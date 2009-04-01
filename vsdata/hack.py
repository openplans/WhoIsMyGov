from __future__ import with_statement
from votesmart import votesmart
from collections import defaultdict
import yaml

votesmart.apikey = 'da3851ba595cbc0d9b5ac5be697714e0'

# Get office types
otypes = dict((otype.officeTypeId, otype.name) for otype in votesmart.office.getTypes())
# Get office levels
olevels = dict((olevel.officeLevelId, olevel.name) for olevel in votesmart.office.getLevels())

# Get office branches
obranches = dict((obranch.officeBranchId, obranch.name) for obranch in votesmart.office.getBranches())

offices = {}

for olevel in olevels:
    for office in votesmart.office.getOfficesByLevel(olevel):
        offices[office.officeId] = offices.get(office.officeId, {})
        offices[office.officeId].update({'name': office.name,
                                         'branch_id': office.officeBranchId,
                                         'branch_name': obranches[office.officeBranchId],
                                         'level_id': office.officeLevelId,
                                         'level_name': olevels[office.officeLevelId],
                                         'type_id': office.officeTypeId,
                                         'type_name': otypes[office.officeTypeId],
                                         'shorttitle': office.shortTitle,
                                         'title': office.title})

with open('offices.yaml','w') as vsout:
    vsout.write(yaml.safe_dump(offices, default_flow_style=False))

states = {"WA": "WASHINGTON",
          "VA": "VIRGINIA",
          "DE": "DELAWARE",
          "WI": "WISCONSIN",
          "WV": "WEST VIRGINIA",
          "HI": "HAWAII",
          "FL": "FLORIDA",
          "WY": "WYOMING",
          "NH": "NEW HAMPSHIRE",
          "NJ": "NEW JERSEY",
          "NM": "NEW MEXICO",
          "TX": "TEXAS",
          "LA": "LOUISIANA",
          "NC": "NORTH CAROLINA",
          "ND": "NORTH DAKOTA",
          "NE": "NEBRASKA",
          "TN": "TENNESSEE",
          "NY": "NEW YORK",
          "PA": "PENNSYLVANIA",
          "CA": "CALIFORNIA",
          "NV": "NEVADA",
          "CO": "COLORADO",
          "AK": "ALASKA",
          "AL": "ALABAMA",
          "AR": "ARKANSAS",
          "VT": "VERMONT",
          "IL": "ILLINOIS",
          "GA": "GEORGIA",
          "IN": "INDIANA",
          "IA": "IOWA",
          "OK": "OKLAHOMA",
          "AZ": "ARIZONA",
          "ID": "IDAHO",
          "CT": "CONNECTICUT",
          "ME": "MAINE",
          "MD": "MARYLAND",
          "MA": "MASSACHUSETTS",
          "OH": "OHIO",
          "UT": "UTAH",
          "MO": "MISSOURI",
          "MN": "MINNESOTA",
          "MI": "MICHIGAN",
          "RI": "RHODE ISLAND",
          "KS": "KANSAS",
          "MT": "MONTANA",
          "MS": "MISSISSIPPI",
          "SC": "SOUTH CAROLINA",
          "KY": "KENTUCKY",
          "OR": "OREGON",
          "SD": "SOUTH DAKOTA"}

districts = {}

for state in states:
    districts[state] = {}
    for office in offices:
        districts[state][office] = []
        try:
            for district in votesmart.district.getByOfficeState(office, state):
                districts[state][office].append((district.name, district.districtId))
        except:
            del(districts[state][office])

with open('districts.yaml','w') as vsout:
    vsout.write(yaml.safe_dump(districts, default_flow_style=False))
