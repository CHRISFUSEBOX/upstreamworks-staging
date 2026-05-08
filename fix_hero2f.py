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

    # Hero row: taller + use flex so columns stretch to fill height
    "\t.vc_custom_1001{min-height:880px !important;}\n"
    "\t.vc_custom_1001>.vc_row-fluid{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\talign-items:stretch !important;\n"
    "\t\tmin-height:inherit !important;\n"
    "\t}\n"
    "\t.vc_custom_1001>.vc_row-fluid>div{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\tflex-direction:column !important;\n"
    "\t}\n"

    # Right column image: fill full column height, lock woman to bottom
    "\t.vc_custom_1004{\n"
    "\t\tmin-height:100% !important;\n"
    "\t\tflex:1 !important;\n"
    "\t\tbackground-position:bottom center !important;\n"
    "\t\tbackground-size:cover !important;\n"
    "\t}\n"

    # Left column: responsive left alignment matching header logo
    "\t.vc_custom_1002{\n"
    "\t\tpadding-left:max(40px,calc((100vw - 1170px) / 2)) !important;\n"
    "\t\tpadding-right:60px !important;\n"
    "\t\tpadding-top:180px !important;\n"
    "\t\tpadding-bottom:100px !important;\n"
    "\t}\n"

    # Headline spacing
    "\t.vc_custom_1001 h1{margin-top:0 !important;margin-bottom:24px !important;}\n"

    # Body text spacing
    "\t.vc_custom_1001 .wpb_text_column{margin-bottom:40px !important;}\n"

    # Button row: flex for equal-height buttons
    "\t.vc_custom_1001 .vc_inner{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\talign-items:stretch !important;\n"
    "\t\tmargin-left:0 !important;\n"
    "\t\tmargin-right:0 !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\tflex-direction:column !important;\n"
    "\t\tpadding-left:0 !important;\n"
    "\t\tpadding-right:12px !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .vc_inner>[class*=vc_col]:last-child{padding-right:0 !important;}\n"
    "\t.vc_custom_1001 .vc_inner .vc_btn3-container{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\tflex:1 !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .vc_inner .vc_btn3{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\tflex:1 !important;\n"
    "\t\talign-items:center !important;\n"
    "\t\tjustify-content:center !important;\n"
    "\t\ttext-align:center !important;\n"
    "\t\tpadding:14px 16px !important;\n"
    "\t\tfont-size:15px !important;\n"
    "\t\tfont-weight:600 !important;\n"
    "\t\tletter-spacing:0.3px !important;\n"
    "\t\twhite-space:normal !important;\n"
    "\t\tline-height:1.3 !important;\n"
    "\t}\n"

    # Tablet
    "\t@media(max-width:991px){\n"
    "\t\t.vc_custom_1001{min-height:820px !important;}\n"
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:max(24px,calc((100vw - 1170px) / 2)) !important;\n"
    "\t\t\tpadding-right:30px !important;\n"
    "\t\t\tpadding-top:140px !important;\n"
    "\t\t\tpadding-bottom:80px !important;\n"
    "\t\t}\n"
    "\t}\n"

    # Mobile
    "\t@media(max-width:767px){\n"
    "\t\t.vc_custom_1001{min-height:auto !important;}\n"
    "\t\t.vc_custom_1001>.vc_row-fluid{flex-direction:column !important;}\n"
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:24px !important;\n"
    "\t\t\tpadding-right:24px !important;\n"
    "\t\t\tpadding-top:100px !important;\n"
    "\t\t\tpadding-bottom:40px !important;\n"
    "\t\t}\n"
    "\t\t.vc_custom_1004{min-height:300px !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner{flex-wrap:wrap !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner>[class*=vc_col]{\n"
    "\t\t\twidth:100% !important;\n"
    "\t\t\tpadding-right:0 !important;\n"
    "\t\t\tpadding-bottom:12px !important;\n"
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
