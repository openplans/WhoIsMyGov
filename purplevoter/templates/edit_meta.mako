<%inherit file="/base.mako" />

<form method="POST" action="${h.url_for(controller="people", action="update_meta", meta_id=c.district_meta.id)}">
  <div class="selfclear">
    <label for="key">Key</label>
    <input id="key" name="key" type="text" value="${c.district_meta.meta_key}" size=50 />
  </div>
  <div class="selfclear">
    <label for="value">Value</label>
    <input id="value" name="value" type="text" value="${c.district_meta.meta_value}" size=50 />
  </div>
  <input type="hidden" name="id" value="${c.district_meta.id}" />
  <input type="hidden" name="referrer" value="${c.referrer}" />
  <div class="selfclear">
    <input class="indented-submit" type="submit" value="Update" />
  </div>
</form>

