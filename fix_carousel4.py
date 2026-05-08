fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

# Remove any previous carousel fallback block
old = content.find('\n// WPBakery carousel fallback')
if old != -1:
    content = content[:old]

# Fix: vcCarousel._build() measures $element.width() as 300px (wrong) at init time.
# On window.load (after vc_carousel.min.js has initialized all carousels), clear the
# stale inline width and re-run resizeAction() so the slideline is sized to the real
# 1410px container instead of 300px.
new_block = (
    "\n"
    "// WPBakery carousel fix: vcCarousel._build() measures a stale 300px inline width\n"
    "// at init time. Clear it on load so resizeAction() uses the real container width.\n"
    "add_action( 'wp_footer', function() {\n"
    "\t$js  = '<script>(function($){';\n"
    "\t$js .= '$(window).on(\"load\",function(){';\n"
    "\t$js .= '$(\".vc_images_carousel\").each(function(){';\n"
    "\t$js .= 'var $el=$(this),inst=$el.data(\"vc.vcCarousel\");';\n"
    "\t$js .= 'if(inst){$el.css(\"width\",\"\");inst.resizeAction();}';\n"
    "\t$js .= '});';\n"
    "\t$js .= '});';\n"
    "\t$js .= '})(jQuery);</script>';\n"
    "\techo $js . \"\\n\";\n"
    "}, 99999 );\n"
)
content += new_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines: ' + str(len(content.splitlines())))
