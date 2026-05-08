-- Migration: Demos and Videos (ID 81399)
-- Rebuilds the page from Elementor (5 sections, 7 videos in 2-col grid + hero banner)
-- into WPBakery shortcode. YouTube IDs preserved; nocookie handled by WP Rocket.
-- Run against: upstreamunix_wp356

-- Step 1: Set post_content to WPBakery shortcode
UPDATE usw_posts SET post_content =
'[vc_row full_width="stretch_row" css=".vc_custom_2101{margin-top:-190px !important;min-height:500px !important;background-image:url(https://stage.upstreamworks.com/wp-content/uploads/2021/02/Upstream-Works-Demos-and-Videos_Banner-F.jpg) !important;background-size:cover !important;background-position:center center !important;background-repeat:no-repeat !important;padding-top:120px !important;padding-bottom:40px !important;}"][vc_column][vc_custom_heading text="DEMOS AND VIDEOS" font_container="tag:h1|text_align:center|color:%23ffffff" use_theme_fonts="yes" css=".vc_custom_2102{margin-bottom:-10px !important;}"][vc_custom_heading text="See Upstream Works Omnichannel Contact Center Solutions in Action" font_container="tag:h3|text_align:center|color:%23ffffff" use_theme_fonts="yes" css=".vc_custom_2103{margin-top:20px !important;margin-bottom:20px !important;}"][vc_btn title="Request a Personalized Demo" style="outline" color="white" size="lg" align="center" css_animation="" link="url:https%3A%2F%2Fstage.upstreamworks.com%2Fdemo%2F"][/vc_column][/vc_row]

[vc_row css=".vc_custom_2110{margin-top:40px !important;margin-bottom:40px !important;}"][vc_column width="1/2" css=".vc_custom_2111{padding-right:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=AndW5OqxuU4" align="center"][vc_column_text]<h2>Upstream Works Power to Innovate</h2>Upstream Works powers innovation and automation. Watch this video to learn how our solutions can benefit contact centers.[/vc_column_text][/vc_column][vc_column width="1/2" css=".vc_custom_2112{padding-left:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=J8WLODCCE9k" align="center"][vc_column_text]<h2>Upstream Works AgentNow in Action</h2>See how AgentNow can be used in a real-life setting, using a kiosk in an airport to provide on-demand customer service to travelers.[/vc_column_text][/vc_column][/vc_row]

[vc_row css=".vc_custom_2120{margin-top:40px !important;margin-bottom:40px !important;}"][vc_column width="1/2" css=".vc_custom_2121{padding-right:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=xdB8MziEhBc" align="center"][vc_column_text]<h2>Meet Upstream Works</h2>A quick introduction to Upstream Works and the value of its solutions.[/vc_column_text][/vc_column][vc_column width="1/2" css=".vc_custom_2122{padding-left:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=kU6WPORku44" align="center"][vc_column_text]<h2>Transforming Agent and Customer Engagements</h2>Personalize customer interactions with a feature-rich omnichannel agent workspace. Empowered Agents. Loyal Customers.[/vc_column_text][/vc_column][/vc_row]

[vc_row css=".vc_custom_2130{margin-top:40px !important;margin-bottom:40px !important;}"][vc_column width="1/2" css=".vc_custom_2131{padding-right:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=hB5rr1YNzfw" align="center"][vc_column_text]<h2>Upstream Works CX &#8211; Redefining Omnichannel</h2>Customer Expectations are changing. Meet these needs with effective, holistic and flexible strategies. It&#8217;s time for a transformed customer experience.[/vc_column_text][/vc_column][vc_column width="1/2" css=".vc_custom_2132{padding-left:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=d2zFdGhjlDc" align="center"][vc_column_text]<h2>Upstream Works in Action &#8211; Utilities</h2>Explore how Upstream Works on Finesse (UWF) is being utilized in the Utilities industry. With an actionable view of the entire customer journey, this company has a thorough understanding of the customer experience, and the power to improve it.[/vc_column_text][/vc_column][/vc_row]

[vc_row css=".vc_custom_2140{margin-top:40px !important;margin-bottom:40px !important;}"][vc_column width="1/2" css=".vc_custom_2141{padding-right:20px !important;}"][vc_video link="https://www.youtube.com/watch?v=8UdTrfabYS0" align="center"][vc_column_text]<h2>Upstream Works in Action &#8211; Insurance</h2>Discover how Insurance companies are maximizing the value of every interaction with effective, efficient, personalized, and proactive member engagement across the enterprise.[/vc_column_text][/vc_column][vc_column width="1/2"][/vc_column][/vc_row]'
WHERE ID = 81399;

-- Step 2: Enable WPBakery renderer
INSERT INTO usw_postmeta (post_id, meta_key, meta_value)
VALUES (81399, '_wpb_vc_js_status', 'true')
ON DUPLICATE KEY UPDATE meta_value = 'true';

-- Step 3: Deactivate Elementor renderer
UPDATE usw_postmeta
SET meta_value = 'inactive'
WHERE meta_key = '_elementor_edit_mode' AND post_id = 81399;

-- Step 4: Delete Elementor CSS cache
DELETE FROM usw_postmeta
WHERE post_id = 81399 AND meta_key IN ('_elementor_css', '_elementor_inline_css');

SELECT 'Demos and Videos migration complete' AS status;
