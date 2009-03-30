<%inherit file="/base.mako" />

<form method="POST" action="/">
  <div class="selfclear">
    <label for="address">Address</label>
    <input id="address" name="address" type="text" />
  </div>
</form>

<!-- temp for testing TODO: MAKE REAL -->
% if c.address_matches:
<ul>
    % for address in c.address_matches:
    <li><a href="/?address=${address}">${address}</a></li>
    % endfor
</ul>
% endif
<p>${c.people}</p>

