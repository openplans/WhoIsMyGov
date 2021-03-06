<%inherit file="/base.mako" />

 <h1>Search in the ${c.election.name} ${c.election.stagename} Election
 of (${c.election.date})</h1>

<form method="GET" action="${request.url}">
  <div class="selfclear">
    <label for="address">Address</label>
    <input id="address" name="address" type="text" value="${c.search_term}" size=50 />
  </div>
  <div class="selfclear">
    <input class="indented-submit" type="submit" value="Find!" />
  </div>
</form>



<div id="search-results">

% if c.address_matches:
<p>Did you mean one of these addresses?</p>
<ul>
    % for address, (lat, lon) in c.address_matches:
    <li><a href="${h.url_for(controller='people', action='search', address=address, lat=lat, lon=lon)}">${address}</a></li>
    % endfor
</ul>
% elif not c.districts:
   <p>No results found.</p>
% else:
 <h2>Results</h2>
 % for district in c.districts:
    <dl class="race">
    % for race in sorted(district.races, key=lambda r: r.office) :
      <dt class="office">Candidates for ${race.office} in
        ${district.district_name},
        % if district.parent_district_name:
	  ${district.parent_district_name}
	% endif
      </dt>
      <dd><dl class="candidate">
      % for person in race.candidates:
        <dt class="fullname"><strong>${person.fullname}</strong></dt>
        <dd>
           % for meta in person.meta:
            <div class="meta">${meta.meta_key}: ${meta.meta_value}</div>
           % endfor
        </dd>
      % endfor           
      </dl></dd>
    % endfor
    </dl>
 % endfor
%endif   

</div>
