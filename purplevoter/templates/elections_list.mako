<%inherit file="/base.mako" />

<h1>Elections</h1>

<div id="search-results">

% if c.elections:
<ul>
    % for election in c.elections:
    <li><a href="/elections/${election.name}-${election.stagename}-${election.date}">
        ${election.date} - ${election.name} - ${election.stagename}</a>
    % endfor
</ul>
% else:
   <p>No results found.</p>
% endif


</div>
