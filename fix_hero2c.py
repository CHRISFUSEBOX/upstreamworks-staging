fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

# Remove previous hero layout CSS block
marker = '\n// Hero layout: responsive alignment + spacing'
old = content.find(marker)
if old != -1:
    content = content[:old]
    print('Removed old hero block')

css_block = (
    "\n"
    "// Hero layout: responsive alignment + spacing\n"
    "add_action( 'wp_head', function() {\n"
    "\t?>\n"
    "\t<style>\n"
    # Responsive left alignment matching header logo: (100vw - 1170px) / 2
    "\t.vc_custom_1002{padding-left:max(40px,calc((100vw - 1170px) / 2)) !important;padding-right:40px !important;}\n"
    # Headline spacing
    "\t.vc_custom_1001 h1{margin-bottom:16px !important;}\n"
    # Subtext spacing before buttons
    "\t.vc_custom_1001 .wpb_text_column{margin-bottom:28px !important;}\n"
    # Button row: remove bootstrap gutter margins, use .vc_inner (WPBakery's actual class)
    "\t.vc_custom_1001 .vc_inner{margin-left:0 !important;margin-right:0 !important;}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]{padding-left:0 !important;padding-right:10px !important;}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]:last-child{padding-right:0 !important;}\n"
    # Button container: override vc_btn3-inline (display:inline-block) → block
    "\t.vc_custom_1001 .vc_inner .vc_btn3-container{display:block !important;}\n"
    # Button itself: fill column, centered, consistent padding
    "\t.vc_custom_1001 .vc_inner .vc_btn3{"
    "display:block !important;"
    "width:100% !important;"
    "text-align:center !important;"
    "padding-top:14px !important;"
    "padding-bottom:14px !important;"
    "white-space:nowrap !important;"
    "font-size:15px !important;"
    "font-weight:600 !important;"
    "}\n"
    # Mobile
    "\t@media(max-width:767px){\n"
    "\t\t.vc_custom_1002{padding-left:24px !important;padding-right:24px !important;padding-top:80px !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner>[class*=vc_col]{padding-right:0 !important;padding-bottom:12px !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner .vc_btn3{white-space:normal !important;}\n"
    "\t}\n"
    "\t</style>\n"
    "\t<?php\n"
    "}, 9999 );\n"
)

content += css_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines:', len(content.splitlines()))
