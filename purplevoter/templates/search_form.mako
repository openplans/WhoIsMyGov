<%inherit file="/base.mako" />

<form method="POST" action="/">
  <div class="selfclear">
    <label for="address">Address</label>
    <input id="address" name="address" type="text" />
  </div>
</form>

<!-- temp for testing TODO: MAKE REAL -->
<p>${c.people}</p>

