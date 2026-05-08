

// WPBakery carousel fallback: WP Rocket async CSS (rocket_pairs) can prevent
// window.load from reaching vc_carousel.min.js registered handler. Priority 999
// ensures this fires last in wp_footer, after all other scripts.
add_action( 'wp_footer', function() {
	echo '<script>(function($){function i(){$("[data-ride=\"vc_carousel\"]").each(function(){var t=$(this);if(!t.data("vc.vcCarousel")&&!t.hasClass("owl-loaded")){t.vcCarousel(t.data());}});}if(document.readyState==="complete"){i();}else{$(window).on("load",i);}})(jQuery);</script>' . "\n";
}, 999 );
