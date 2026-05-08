fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

# Remove any previous carousel fallback block
old = content.find('\n// WPBakery carousel fallback')
if old != -1:
    content = content[:old]

# Fix: init immediately (handles cases where load already fired), then on window.load
# refresh any owl-loaded carousels so Owl recalculates width against the fully-laid-out container.
new_block = (
    "\n"
    "// WPBakery carousel fallback: vc_per-view-more carousels need vcOwlCarousel(),\n"
    "// not vcCarousel(). Init immediately in footer, then refresh on load so Owl\n"
    "// recalculates item widths against the fully-rendered container (avoids 300px init bug).\n"
    "add_action( 'wp_footer', function() {\n"
    "\t$js  = '<script>(function($){';\n"
    "\t$js .= 'function i(){';\n"
    "\t$js .= '$(\".vc_images_carousel\").each(function(){';\n"
    "\t$js .= 'var t=$(this);';\n"
    "\t$js .= 'if(t.hasClass(\"vc_per-view-more\")&&!t.hasClass(\"owl-loaded\")){t.vcOwlCarousel();}';\n"
    "\t$js .= 'else if(!t.data(\"vc.vcCarousel\")&&!t.hasClass(\"owl-loaded\")){t.vcCarousel(t.data());}';\n"
    "\t$js .= '});}';\n"
    "\t$js .= 'i();';\n"
    "\t$js .= '$(window).on(\"load\",function(){';\n"
    "\t$js .= 'i();';\n"
    "\t$js .= '$(\".vc_images_carousel.owl-loaded\").trigger(\"refresh.owl.carousel\");';\n"
    "\t$js .= '});';\n"
    "\t$js .= '})(jQuery);</script>';\n"
    "\techo $js . \"\\n\";\n"
    "}, 999 );\n"
)
content += new_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines: ' + str(len(content.splitlines())))
