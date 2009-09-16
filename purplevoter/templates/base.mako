<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://gmpg.org/xfn/11">
    <style type="text/css" media="screen">
    /*<![CDATA[ */
    @import'${h.url_for('/style.css')}';
    /* ]]> */
    </style>
</head>
<body>
  <div id="container" class="selfclear">
    <div id="header">
       <h1 id="logo">Who Is My Government?<sup>ALPHA</sup></h1>
       <h3 id="tag-line">Find out who represents you.</h3>
    </div>
    <div id="main">
      <div id="content">
          ${next.body()}
      </div>
    </div>
</body>
</html>

