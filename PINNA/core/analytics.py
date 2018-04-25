"""
PINNA
google-analytics.py

Created by Shota Shimazu on 2018/03/16

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://bitbucket.org/mixstage/pinna-serveur/src/master/LICENSE
"""

import textwrap

class GoogleAnalytics():
    pass

script_template = '''
<!-- Google Analytics -->
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', '{GA_ID}', 'auto');
ga('send', 'pageview');
</script>
<!-- End Google Analytics -->
'''.textwrap(
    GA_ID = "TEST ID"
)
