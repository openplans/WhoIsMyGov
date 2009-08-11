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
   <dl>
   % for person in district.people:
     <dt class="district">${district.level_name}: ${person.office}: ${district.district_name}</dt>
     <dd class="fullname">
        <div class="fullname">Name: <strong>${person.fullname}</strong></div>
         % for meta in person.meta:
          <div class="meta">${meta.meta_key}: ${meta.meta_value}</div>
         % endfor
     </dd>
   % endfor
   </dl>

% endfor
</div>
