import subprocess, sys

DB = 'upstreamunix_wp356'
PFX = 'usw_'
CMD = 'mysql -u upstreamunix_wp356 -p"PASS" ' + DB

def q(sql):
    r = subprocess.run(['mysql', '-u', 'upstreamunix_wp356', '-pp-zg22@S02', DB, '-sN', '-e', sql],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.stdout.decode('utf-8').strip()

# Find front page ID
front_id = q("SELECT option_value FROM {0}options WHERE option_name='page_on_front'".format(PFX))
print('Front page ID:', front_id)

# Read post_content
content = q("SELECT post_content FROM {0}posts WHERE ID={1}".format(PFX, front_id))
# Find the hero column with buttons
lines = content.split('[vc_btn3')
print('\n=== vc_btn3 shortcodes ===')
for i, part in enumerate(lines[1:], 1):
    end = part.find(']')
    print(f'\n--- Button {i} ---')
    print('[vc_btn3' + part[:end+1])

# Read custom CSS
css = q("SELECT meta_value FROM {0}postmeta WHERE post_id={1} AND meta_key='_wpb_shortcodes_custom_css'".format(PFX, front_id))
print('\n=== _wpb_shortcodes_custom_css ===')
print(css)
