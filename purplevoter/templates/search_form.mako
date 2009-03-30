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
    % for address in c.address_matches:
    <li><a href="${h.url_for(controller='people', action='search', address=address)}">${address}</a></li>
    % endfor
</ul>
% endif

% for level in c.people:
    <h2>${level} District: ${c.people[level]['display_name']}</h2>
% endfor
</div>
