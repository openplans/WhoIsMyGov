<%inherit file="/base.mako" />

<form method="POST" action="${h.url_for(controller="people", action="delete_meta", meta_id=c.district_meta.id)}">
  <div class="selfclear">
     Are you sure that you want to delete this information?
  </div>
  <input type="hidden" name="id" value="${c.district_meta.id}" />
  <input type="hidden" name="referrer" value="${c.referrer}" />
  <div class="selfclear">
    <input type="submit" value="Delete" />
  </div>
</form>

