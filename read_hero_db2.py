import subprocess

DB = 'upstreamunix_wp356'
PFX = 'usw_'
PW = 'p-zg22@S02'

def q(sql):
    r = subprocess.run(['mysql', '-u', 'upstreamunix_wp356', '-p' + PW, DB, '-sN', '-e', sql],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.stdout.decode('utf-8').strip()

front_id = '81046'

# Dump raw post_content first 3000 chars
content = q("SELECT post_content FROM {0}posts WHERE ID={1}".format(PFX, front_id))
print('=== post_content (first 3000 chars) ===')
print(content[:3000])
print('\n...\n')
print('Total length:', len(content))

# Check if there's a vc_btn3 anywhere
idx = content.find('vc_btn3')
print('vc_btn3 first occurrence at index:', idx)
if idx != -1:
    print(content[max(0,idx-50):idx+300])
