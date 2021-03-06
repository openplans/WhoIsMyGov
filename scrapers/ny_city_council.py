#!/usr/bin/env python

import urllib
from lxml.html import parse
import re
import pprint

STRIPPER = re.compile('[\\s\xa0]+')

def scrape_members():
    """ Scrape the city council member information from the NY City Council website """
    council_members_url = 'http://council.nyc.gov/html/members/members.shtml'
    doc = parse(council_members_url).getroot()
    doc.make_links_absolute()
    members = []
    headers = [STRIPPER.sub(' ', header.text_content().lower()) for header in doc.cssselect('#members_table tr#header th')]
    columns = dict((value, index + 1) for (index, value) in enumerate(headers))
    for row in doc.cssselect('#members_table tr'):
        if row.get('id') == 'header':
            continue
        member = {}
        for column, index in columns.iteritems():
            #print column
            if not column.strip(): # skip whitespace column
                continue
            field_data = row.cssselect('td:nth-child(%d)' % index)[0]
            if column == 'name':
               member['href'] = field_data.cssselect('a')[0].attrib['href']
            member[column] = field_data.text_content()

        members.append(member)
    pprint.pprint( sorted(members, key=lambda x: int(x['district'])))
            
    

if __name__ == '__main__':
    scrape_members()
