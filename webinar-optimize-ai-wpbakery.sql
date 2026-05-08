-- Migration: Webinar: Optimize AI, Video Engagements & Webex Contact Center (ID 86259)
-- Elementor data already contained WPBakery shortcode inside a text-editor widget.
-- This extracts that content directly into post_content and switches renderer to WPBakery.
-- Run against: upstreamunix_wp356

-- Step 1: Set post_content to the extracted WPBakery shortcode
UPDATE usw_posts SET post_content =
'[vc_row][vc_column width="1/2" css=".vc_custom_1644265436653{margin-top: -30px !important;margin-left: -20px !important;padding-top: 40px !important;padding-bottom: 10px !important;}"][vc_column_text]<h2><span style="color: #0777be;">Demo Webinar: Optimize AI, Video Engagements &amp; Webex Contact Center</span></h2>[/vc_column_text][vc_column_text css=".vc_custom_1687280776776{margin-top: -5px !important;}"]Join us for a demo webinar to see our new features that help contact centers optimize AI, personalize CX with Webex Video solutions, and our new platform offering, Upstream Works on Webex Contact Center (UWW).

<p style="text-align: left;">Date: Thursday, July 13, 2023</p>
<p style="text-align: left;">Time: 8 am PT | 11 am ET | 4 pm GMT</p>

<strong>During the webinar, we\'ll cover:</strong>
<ul>
<li>How to Optimize AI with our Bot Experimentation Framework and Chatbot capabilities</li>
<li>The new Omnichannel Dashboard and KPIs that enable quick visibility and fast action</li>
<li>Better real-time engagements with Webex Connect and Webex Video solutions</li>
<li>Ease of migration with our new platform offering on Webex Contact Center</li>
</ul>
[/vc_column_text][/vc_column][vc_column width="1/2" css=".vc_custom_1644261775810{margin-top: 10px !important;margin-left: 60px !important;}"][vc_column_text]<h2 style="text-align: center;"><span style="color: #0777be;">Register Today!</span></h2>[/vc_column_text][vc_raw_html]JTNDZGl2JTIwaWQlM0QlMjJNQWZvcm0tMTViNjgxZTctZWZhNy00N2YwLWE4Y2QtNDNjZGEzN2VlN2I1JTIyJTIwY2xhc3MlM0QlMjJNQWZvcm0lMjIlM0UlMEElMDklM0NzY3JpcHQlMjB0eXBlJTNEJTIydGV4dCUyRmphdmFzY3JpcHQlMjIlMjBzcmMlM0QlMjJodHRwcyUzQSUyRiUyRmZvcm1zLm5ldC1yZXN1bHRzLmlvJTJGZm9ybS1yZW5kZXIuanMlM0ZmaWQlM0QxNWI2ODFlNy1lZmE3LTQ3ZjAtYThjZC00M2NkYTM3ZWU3YjUlMjIlMjBjcm9zc29yaWdpbiUzRCUyMmFub255bW91cyUyMiUzRSUzQyUyRnNjcmlwdCUzRSUwQSUzQyUyRmRpdiUzRQ==[/vc_raw_html][/vc_column][/vc_row]
[vc_row full_width="stretch_row" css=".vc_custom_1683651279455{background-color: #0777be !important;}"][vc_column][vc_column_text]<h4 class="bio-title" style="text-align: center;"><b>Featured Speakers</b></h4>[/vc_column_text][/vc_column][/vc_row]
[vc_row full_width="stretch_row" css=".vc_custom_1683651287175{background-color: #0777be !important;}"][vc_column width="1/3" css=".vc_custom_1683651698070{margin-top: -20px !important;}"][vc_single_image image="81817" alignment="center"][vc_column_text]<h4 class="bio-title" style="text-align: center;"><b>Jeff Palmer</b><br /><strong>CRO</strong><br /><strong>Upstream Works</strong></h4>[/vc_column_text][/vc_column][vc_column width="1/3" css=".vc_custom_1683651689324{margin-top: -20px !important;margin-left: -10px !important;}"][vc_single_image image="82413" alignment="center"][vc_column_text]<h4 class="bio-title" style="text-align: center;"><b>Matt Felix</b><br /><strong>Solutions Engineer</strong><br /><strong>Upstream Works</strong></h4>[/vc_column_text][/vc_column][vc_column width="1/3" css=".vc_custom_1683651681400{margin-top: -20px !important;}"][vc_single_image image="82412" alignment="center"][vc_column_text]<h4 class="bio-title" style="text-align: center;"><b>Simon Newbury</b><br /><strong>Solutions Engineer</strong><br /><strong>Upstream Works</strong></h4>[/vc_column_text][/vc_column][/vc_row]'
WHERE ID = 86259;

-- Step 2: Enable WPBakery renderer
INSERT INTO usw_postmeta (post_id, meta_key, meta_value)
VALUES (86259, '_wpb_vc_js_status', 'true')
ON DUPLICATE KEY UPDATE meta_value = 'true';

-- Step 3: Deactivate Elementor renderer
UPDATE usw_postmeta
SET meta_value = 'inactive'
WHERE meta_key = '_elementor_edit_mode' AND post_id = 86259;

-- Step 4: Delete Elementor CSS cache for this post
DELETE FROM usw_postmeta
WHERE post_id = 86259 AND meta_key IN ('_elementor_css', '_elementor_inline_css');

SELECT 'Webinar migration complete' AS status;
