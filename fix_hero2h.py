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

    # ── Desktop base (1170px+) ──────────────────────────────────────────────

    "\t.vc_custom_1001{min-height:880px !important;}\n"

    # Right column image: match hero height, woman anchored to bottom
    "\t.vc_custom_1004{\n"
    "\t\tmin-height:880px !important;\n"
    "\t\tbackground-position:bottom center !important;\n"
    "\t\tbackground-size:cover !important;\n"
    "\t}\n"

    # Left column alignment + spacing
    "\t.vc_custom_1002{\n"
    "\t\tpadding-left:max(40px,calc((100vw - 1170px) / 2)) !important;\n"
    "\t\tpadding-right:60px !important;\n"
    "\t\tpadding-top:180px !important;\n"
    "\t\tpadding-bottom:100px !important;\n"
    "\t}\n"

    # Headline: fluid scaling — 48px at 1170px+, scales down with viewport
    "\t.vc_custom_1001 h1{\n"
    "\t\tfont-size:clamp(26px,4vw,48px) !important;\n"
    "\t\tline-height:1.2 !important;\n"
    "\t\tmargin-top:0 !important;\n"
    "\t\tmargin-bottom:20px !important;\n"
    "\t}\n"

    # Body text: fluid scaling
    "\t.vc_custom_1001 .wpb_text_column p{\n"
    "\t\tfont-size:clamp(16px,1.8vw,24px) !important;\n"
    "\t\tline-height:1.4 !important;\n"
    "\t\tmargin-bottom:0 !important;\n"
    "\t}\n"
    "\t.vc_custom_1001 .wpb_text_column{margin-bottom:36px !important;}\n"

    # Button row: equal-height flex
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
    "\t.vc_custom_1001 .vc_inner .vc_btn3-container{display:flex !important;flex:1 !important;}\n"
    "\t.vc_custom_1001 .vc_inner .vc_btn3{\n"
    "\t\tdisplay:flex !important;\n"
    "\t\tflex:1 !important;\n"
    "\t\talign-items:center !important;\n"
    "\t\tjustify-content:center !important;\n"
    "\t\ttext-align:center !important;\n"
    "\t\tpadding:14px 12px !important;\n"
    "\t\tfont-size:14px !important;\n"
    "\t\tfont-weight:600 !important;\n"
    "\t\twhite-space:normal !important;\n"
    "\t\tline-height:1.3 !important;\n"
    "\t}\n"

    # ── Tablet 768–1169px ───────────────────────────────────────────────────
    "\t@media(max-width:1169px) and (min-width:768px){\n"
    "\t\t.vc_custom_1001{min-height:820px !important;}\n"
    "\t\t.vc_custom_1004{min-height:820px !important;}\n"
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:40px !important;\n"
    "\t\t\tpadding-right:30px !important;\n"
    "\t\t\tpadding-top:160px !important;\n"
    "\t\t\tpadding-bottom:80px !important;\n"
    "\t\t}\n"
    "\t}\n"

    # ── Mobile <768px ───────────────────────────────────────────────────────
    "\t@media(max-width:767px){\n"
    # Columns stack — hero height becomes auto
    "\t\t.vc_custom_1001{min-height:auto !important;}\n"
    # Woman image stacks below, top-anchored on mobile
    "\t\t.vc_custom_1004{\n"
    "\t\t\tmin-height:280px !important;\n"
    "\t\t\tbackground-position:top center !important;\n"
    "\t\t}\n"
    # Left column: full bleed padding, enough top to clear sticky header
    "\t\t.vc_custom_1002{\n"
    "\t\t\tpadding-left:20px !important;\n"
    "\t\t\tpadding-right:20px !important;\n"
    "\t\t\tpadding-top:100px !important;\n"
    "\t\t\tpadding-bottom:40px !important;\n"
    "\t\t}\n"
    # Headline: larger min at mobile for readability
    "\t\t.vc_custom_1001 h1{\n"
    "\t\t\tfont-size:clamp(28px,7vw,40px) !important;\n"
    "\t\t}\n"
    "\t\t.vc_custom_1001 .wpb_text_column p{\n"
    "\t\t\tfont-size:clamp(15px,4vw,18px) !important;\n"
    "\t\t}\n"
    # Buttons: wrap to column, full width, stacked
    "\t\t.vc_custom_1001 .vc_inner{flex-direction:column !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner>[class*=vc_col]{\n"
    "\t\t\twidth:100% !important;\n"
    "\t\t\tpadding-right:0 !important;\n"
    "\t\t\tpadding-bottom:10px !important;\n"
    "\t\t}\n"
    "\t\t.vc_custom_1001 .vc_inner>[class*=vc_col]:last-child{padding-bottom:0 !important;}\n"
    "\t\t.vc_custom_1001 .vc_inner .vc_btn3{\n"
    "\t\t\tpadding:14px 20px !important;\n"
    "\t\t\tfont-size:15px !important;\n"
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
