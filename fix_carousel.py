fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

old = content.find('\n// WPBakery carousel fallback')
if old != -1:
    content = content[:old]

new_block = (
    "\n"
    "// WPBakery carousel fallback: window.load race with WP Rocket async CSS.\n"
    "// Calls i() immediately in footer (all scripts loaded) + on load for sizing.\n"
    "add_action( 'wp_footer', function() {\n"
    "\t$js = '<script>(function($){';\n"
    "\t$js .= 'function i(){';\n"
    "\t$js .= '$(\"[data-ride=\\\\\"vc_carousel\\\\\"]\").each(function(){';\n"
    "\t$js .= 'var t=$(this);';\n"
    "\t$js .= 'if(!t.data(\"vc.vcCarousel\")&&!t.hasClass(\"owl-loaded\")){t.vcCarousel(t.data());}';\n"
    "\t$js .= '});}';\n"
    "\t$js .= 'i();$(window).on(\"load\",i);';\n"
    "\t$js .= '})(jQuery);</script>';\n"
    "\techo $js . \"\\n\";\n"
    "}, 999 );\n"
)
content += new_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines: ' + str(len(content.splitlines())))
