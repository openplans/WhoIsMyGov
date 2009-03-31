<%inherit file="/base.mako" />

<form method="POST" action="/">
  <div class="selfclear">
    <label for="address">Address</label>
    <input id="address" name="address" type="text" />
  </div>
</form>


<div id="search-results">
% if c.address_matches:
<ul>
    % for address, (lat, lon) in c.address_matches:
    <li><a href="${h.url_for(controller='people', action='search', address=address, lat=lat, lon=lon)}">${address}</a></li>
    % endfor
</ul>
% endif

% for district in c.districts:
   <h2>${district.level_type}</h2>
   <dl id="district-meta">
      <dt><strong>District Name</strong></dt>
      <dd>${district.district_name}</dd>
      % for meta in district.meta:
          <dt><strong>${meta.meta_key}</strong></dt>
          <dt>${meta.meta_value}</dt>
      % endfor
   </dl>
% endfor
</div>
