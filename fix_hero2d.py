fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

marker = '\n// Hero layout: responsive alignment + spacing'
old = content.find(marker)
if old != -1:
    content = content[:old]

css_block = (
    "\n"
    "// Hero layout: responsive alignment + spacing\n"
    "add_action( 'wp_head', function() {\n"
    "\t?>\n"
    "\t<style>\n"
    # Responsive left alignment matching header logo: (100vw - 1170px) / 2
    "\t.vc_custom_1002{\n"
    "\t\tpadding-left:max(40px,calc((100vw - 1170px) / 2)) !important;\n"
    "\t\tpadding-right:60px !important;\n"
    "\t\tpadding-top:180px !important;\n"
    "\t\tpadding-bottom:80px !important;\n"
    "\t}\n"
    # Headline: tight bottom, good line-height
    "\t.vc_custom_1001 h1{\n"
    "\t\tmargin-top:0 !important;\n"
    "\t\tmargin-bottom:24px !important;\n"
    "\t}\n"
    # Body text paragraph: more room before buttons
    "\t.vc_custom_1001 .wpb_text_column{\n"
    "\t\tmargin-bottom:40px !important;\n"
    "\t}\n"
    # Inner button row: flush with content
    "\t.vc_custom_1001 .vc_inner{\n"
    "\t\tmargin-left:0 !important;\n"
    "\t\tmargin-right:0 !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]{\n"
    "\t\tpadding-left:0 !important;\n"
    "\t\tpadding-right:12px !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]:last-child{\n"
    "\t\tpadding-right:0 !important;\n"
    "\t}\n"
    # Button container: block
    "\t.vc_custom_1001 .vc_inner .vc_btn3-container{\n"
    "\t\tdisplay:block !important;\n"
    "\t}\n"
    # Button: fill column, tall, bold, no-wrap
    "\t.vc_custom_1001 .vc_inner .vc_btn3{\n"
    "\t\tdisplay:block !important;\n"
    "\t\twidth:100% !important;\n"
    "\t\ttext-align:center !important;\n"
    "\t\tpadding-top:16px !important;\n"
    "\t\tpadding-bottom:16px !important;\n"
    "\t\tpadding-left:12px !important;\n"
    "\t\tpadding-right:12px !important;\n"
    "\t\twhite-space:nowrap !important;\n"
    "\t\tfont-size:15px !important;\n"
    "\t\tfont-weight:600 !important;\n"
    "\t\tletter-spacing:0.3px !important;\n"
    "\t}\n"
    # Mobile
    "\t@media(max-width:991px){\n"
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:max(24px,calc((100vw - 1170px) / 2)) !important;\n"
    "\t\t\tpadding-right:24px !important;\n"
    "\t\t\tpadding-top:120px !important;\n"
    "\t\t}\n"
    "\t}\n"
    "\t@media(max-width:767px){\n"
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:24px !important;\n"
    "\t\t\tpadding-right:24px !important;\n"
    "\t\t\tpadding-top:80px !important;\n"
    "\t\t}\n"
    "\t\t.vc_custom_1001 .vc_inner>[class*=vc_col]{\n"
    "\t\t\tpadding-right:0 !important;\n"
    "\t\t\tpadding-bottom:12px !important;\n"
    "\t\t}\n"
    "\t\t.vc_custom_1001 .vc_inner .vc_btn3{\n"
    "\t\t\twhite-space:normal !important;\n"
    "\t\t}\n"
    "\t}\n"
    "\t</style>\n"
    "\t<?php\n"
    "}, 9999 );\n"
)

content += css_block

with open(fn, 'w') as f:
    f.write(content)
print('Done, lines:', len(content.splitlines()))
