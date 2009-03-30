<%inherit file="/base.mako" />

<form method="POST" action="/">
  <div class="selfclear">
    <label for="address">Address</label>
    <input id="address" name="address" type="text" />
  </div>
</form>

<!-- temp for testing TODO: MAKE REAL -->
% for level in c.people:
    <h2>${level} District: ${c.people[level]['display_name']}</h2>
% endfor

