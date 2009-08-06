<%inherit file="/base.mako" />

<form method="GET" action="/">
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
% endif

% for district in c.districts:
   <h2>${district.level_name}: ${district.district_type}</h2>
   <dl id="district-meta">
      <dt><strong>District Name</strong></dt>
      <dd>${district.district_name}</dd>
      % for person in district.people:
          <dt><strong>Name</strong></dt>
          <dd>${person.fullname}</dd>
      % endfor
   </dl>
% endfor
</div>
