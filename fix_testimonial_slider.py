fn = '/home/upstreamunix/stage.upstreamworks.com/wp-content/themes/upstreamworks/functions.php'
with open(fn, 'r') as f:
    content = f.read()

marker = '\n// Testimonial slider enqueue'
if marker in content:
    print('Already present — nothing to do.')
else:
    block = r"""
// Testimonial slider enqueue
add_action( 'wp_enqueue_scripts', function() {
	wp_enqueue_script(
		'testimonial-slider',
		get_template_directory_uri() . '/javascripts/testimonial-slider.js',
		array( 'jquery' ),
		filemtime( get_template_directory() . '/javascripts/testimonial-slider.js' ),
		true
	);
} );
"""
    content += block
    with open(fn, 'w') as f:
        f.write(content)
    print('Done, lines:', len(content.splitlines()))
