fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

# Remove any previous hero layout CSS block
marker = '\n// Hero layout: responsive alignment + spacing'
old = content.find(marker)
if old != -1:
    content = content[:old]

css_block = (
    "\n"
    "// Hero layout: responsive alignment + spacing\n"
    "add_action( 'wp_head', function() {\n"
    "\techo '<style>\n"

    # Responsive left alignment matching the header logo position:
    # logo is at (100vw - 1170px) / 2 from left edge
    ".vc_custom_1002{"
    "padding-left:max(40px,calc((100vw - 1170px) / 2)) !important;"
    "padding-right:40px !important;"
    "}\n"

    # h1: tighten bottom margin so it sits close to subtext
    ".vc_custom_1001 h1{margin-bottom:16px !important;}\n"

    # Subtext: more space before buttons
    ".vc_custom_1001 .wpb_text_column{margin-bottom:32px !important;}\n"

    # Remove left gap introduced by row_inner bootstrap padding
    ".vc_custom_1001 .vc_row_inner{margin-left:0 !important;margin-right:0 !important;}\n"

    # Button columns: remove horizontal gutter so buttons align flush left
    ".vc_custom_1001 .vc_row_inner>[class*=vc_col]{"
    "padding-left:0 !important;padding-right:12px !important;}\n"
    ".vc_custom_1001 .vc_row_inner>[class*=vc_col]:last-child{padding-right:0 !important;}\n"

    # Buttons: block + fill column width + equal height padding
    ".vc_custom_1001 .vc_row_inner .vc_btn3{"
    "display:block !important;"
    "width:100% !important;"
    "text-align:center !important;"
    "padding-top:14px !important;"
    "padding-bottom:14px !important;"
    "white-space:nowrap !important;"
    "font-size:16px !important;"
    "}\n"

    # Mobile
    "@media(max-width:767px){"
    ".vc_custom_1002{padding-left:24px !important;padding-right:24px !important;padding-top:80px !important;}"
    ".vc_custom_1001 .vc_row_inner>[class*=vc_col]{padding-right:0 !important;padding-bottom:12px !important;}"
    ".vc_custom_1001 .vc_row_inner .vc_btn3{white-space:normal !important;}"
    "}\n"

    "' 99 );\n"
)

# Fix closing — the echo needs proper PHP closing
css_block = (
    "\n"
    "// Hero layout: responsive alignment + spacing\n"
    "add_action( 'wp_head', function() {\n"
    "\t?>\n"
    "\t<style>\n"
    "\t.vc_custom_1002{padding-left:max(40px,calc((100vw - 1170px) / 2)) !important;padding-right:40px !important;}\n"
    "\t.vc_custom_1001 h1{margin-bottom:16px !important;}\n"
    "\t.vc_custom_1001 .wpb_text_column{margin-bottom:32px !important;}\n"
    "\t.vc_custom_1001 .vc_row_inner{margin-left:0 !important;margin-right:0 !important;}\n"
    "\t.vc_custom_1001 .vc_row_inner>[class*=vc_col]{padding-left:0 !important;padding-right:12px !important;}\n"
    "\t.vc_custom_1001 .vc_row_inner>[class*=vc_col]:last-child{padding-right:0 !important;}\n"
    "\t.vc_custom_1001 .vc_row_inner .vc_btn3{display:block !important;width:100% !important;text-align:center !important;padding-top:14px !important;padding-bottom:14px !important;white-space:nowrap !important;font-size:16px !important;}\n"
    "\t@media(max-width:767px){\n"
    "\t\t.vc_custom_1002{padding-left:24px !important;padding-right:24px !important;padding-top:80px !important;}\n"
    "\t\t.vc_custom_1001 .vc_row_inner>[class*=vc_col]{padding-right:0 !important;padding-bottom:12px !important;}\n"
    "\t\t.vc_custom_1001 .vc_row_inner .vc_btn3{white-space:normal !important;}\n"
    "\t}\n"
    "\t</style>\n"
    "\t<?php\n"
    "}, 99 );\n"
)

content += css_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines:', len(content.splitlines()))
