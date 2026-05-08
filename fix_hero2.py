import subprocess, re

DB = 'upstreamunix_wp356'
PFX = 'usw_'
PW = 'p-zg22@S02'
POST_ID = '81046'

def q(sql):
    r = subprocess.run(['mysql', '-u', 'upstreamunix_wp356', '-p' + PW, DB, '-sN', '-e', sql],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = r.stdout.decode('utf-8').strip()
    err = r.stderr.decode('utf-8').strip()
    if err and 'Warning' not in err:
        print('ERROR:', err)
    return out

def u(sql):
    r = subprocess.run(['mysql', '-u', 'upstreamunix_wp356', '-p' + PW, DB, '-e', sql],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = r.stderr.decode('utf-8').strip()
    if err and 'Warning' not in err:
        print('ERROR:', err)
    return r.returncode

# ── 1. Update post_content ──────────────────────────────────────────────────

content = q("SELECT post_content FROM {0}posts WHERE ID={1}".format(PFX, POST_ID))

# 1a. Align text left edge with logo (135px viewport; Bootstrap col adds 15px = 120px needed)
content = content.replace(
    'padding-left:40px !important;}"][vc_custom_heading',
    'padding-left:120px !important;}"][vc_custom_heading'
)

# 1b. Tour AgentNow: color="primary" → color="success" + green CSS
content = content.replace(
    '[vc_btn title="Tour AgentNow" color="primary" size="lg"',
    '[vc_btn title="Tour AgentNow" color="success" size="lg" css=".vc_custom_1005{background-color:#69BA07 !important;border-color:#69BA07 !important;}"'
)

# 1c. Book a Dream Workshop: outline/white → modern/success + green CSS
content = content.replace(
    '[vc_btn title="Book a Dream Workshop" style="outline" color="white" size="lg"',
    '[vc_btn title="Book a Dream Workshop" style="modern" color="success" size="lg" css=".vc_custom_1006{background-color:#69BA07 !important;border-color:#69BA07 !important;}"'
)

# Verify changes were made
assert 'padding-left:120px' in content, 'padding-left change failed'
assert 'vc_custom_1005' in content, 'Tour AgentNow change failed'
assert 'vc_custom_1006' in content, 'Book a Dream Workshop change failed'
print('post_content changes verified OK')

escaped = content.replace('\\', '\\\\').replace("'", "\\'")
ret = u("UPDATE {0}posts SET post_content='{1}' WHERE ID={2}".format(PFX, escaped, POST_ID))
print('post_content updated, return code:', ret)

# ── 2. Update _wpb_shortcodes_custom_css ───────────────────────────────────

css = q("SELECT meta_value FROM {0}postmeta WHERE post_id={1} AND meta_key='_wpb_shortcodes_custom_css'".format(PFX, POST_ID))

# 2a. Update padding-left 80px → 120px in vc_custom_1002
css = css.replace(
    '.vc_custom_1002{padding-top:160px !important;padding-bottom:60px !important;padding-left:80px !important;}',
    '.vc_custom_1002{padding-top:160px !important;padding-bottom:60px !important;padding-left:120px !important;}'
)

# 2b. Remove the outline button rule added in fix 1 (no longer needed)
css = css.replace(
    '.vc_custom_1001 .vc_btn3.vc_btn3-style-outline.vc_btn3-color-white{border:2px solid rgba(255,255,255,0.9) !important;background:rgba(255,255,255,0.12) !important;font-weight:600 !important;}',
    ''
)

# 2c. Add green CSS for new button classes + mobile stacking
new_rules = (
    '.vc_custom_1005{background-color:#69BA07 !important;border-color:#69BA07 !important;}'
    '.vc_custom_1006{background-color:#69BA07 !important;border-color:#69BA07 !important;}'
    '@media(max-width:767px){'
    '.vc_custom_1001 .vc_btn3{display:block !important;width:100% !important;text-align:center !important;margin-bottom:10px !important;}'
    '}'
)
css += new_rules

assert 'padding-left:120px' in css, 'CSS padding-left change failed'
assert 'vc_custom_1005' in css, 'vc_custom_1005 missing'
assert 'vc_custom_1006' in css, 'vc_custom_1006 missing'
assert 'max-width:767px' in css, 'mobile CSS missing'
print('_wpb_shortcodes_custom_css changes verified OK')

escaped_css = css.replace('\\', '\\\\').replace("'", "\\'")
ret2 = u("UPDATE {0}postmeta SET meta_value='{1}' WHERE post_id={2} AND meta_key='_wpb_shortcodes_custom_css'".format(PFX, escaped_css, POST_ID))
print('_wpb_shortcodes_custom_css updated, return code:', ret2)

print('All done.')
