<?php


/**
 * @package WordPress
 * @subpackage Default_Theme
 */

$content_width = 450;
add_theme_support( 'post-thumbnails'); 
//add_image_size( 'featured-img', 117, 114, true );


/********************************************************************************************
 **************************   This is used for create sidebar( widget)      *****************
/********************************************************************************************/
if ( function_exists('register_sidebar') ) {	
	//sidebar Widget
	register_sidebar(array(
		'name'          => __( 'Sidebar', 'theme_text_domain' ),
		'id'            => 'sidebar',
		'before_widget' => '<div id="%1$s" class="widget %2$s">',
		'after_widget' => '</div>',
		'before_title' => '<h2 class="widgettitle">',
		'after_title' => '</h2>',
	));
    register_sidebar(array(
		'name'          => __( 'Footer Menu', 'theme_text_domain' ),
		'id'            => 'footermenu',
		'before_widget' => '<nav class="link">',
		'after_widget'  => '</nav>',
		'before_title'  => '<h3>',
		'after_title'   => '</h3>',
	));
	
	register_sidebar(array(
		'name'          => __( 'Blog', 'theme_text_domain' ),
		'id'            => 'blog',
		'before_widget' => '<div class="text">',
		'after_widget'  => '</div>',
		'before_title'  => '<h3>',
		'after_title'   => '</h3>',
	));
	
	register_sidebar(array(
		'name'          => __( 'User Stories', 'theme_text_domain' ),
		'id'            => 'userstories',
		'before_widget' => '<div class="text">',
		'after_widget'  => '</div>',
		'before_title'  => '<h3>',
		'after_title'   => '</h3>',
	));
	
	register_sidebar(array(
		'name'          => __( 'Events', 'theme_text_domain' ),
		'id'            => 'events',
		'before_widget' => '<div class="text">',
		'after_widget'  => '</div>',
		'before_title'  => '<h3>',
		'after_title'   => '</h3>',
	));
}

/********************************************************************************************
 **************************   This function is used for add js and css      *****************
/********************************************************************************************/
add_action( 'wp_enqueue_scripts', 'add_theme_scripts');
function add_theme_scripts() {

  //Adding css file 
  wp_enqueue_style( 'style', get_stylesheet_uri());
  wp_enqueue_style( 'hind-font', 'https://fonts.googleapis.com/css?family=Hind:400,300,500,600,700');
  wp_enqueue_style( 'Montserrat-font', 'https://fonts.googleapis.com/css?family=Montserrat:400,700');
  wp_enqueue_style( 'fonts-css', get_template_directory_uri().'/fonts/fonts.css');
  wp_enqueue_style( 'font-aw', get_template_directory_uri().'/font-awesome/css/font-awesome.min.css');
  wp_enqueue_style( 'bootstrap-css', get_template_directory_uri().'/stylesheets/bootstrap.min.css');	  
  wp_enqueue_style( 'mmenu-css', get_template_directory_uri().'/stylesheets/jquery.mmenu.all.css'); 		  
  wp_enqueue_style( 'global-css', get_template_directory_uri().'/stylesheets/global.css');    
  wp_enqueue_style( 'device-css', get_template_directory_uri().'/stylesheets/device.css');
  
  //Adding js file
  wp_enqueue_script( 'jquery' );
  wp_enqueue_script( 'mmenu-js', get_template_directory_uri().'/javascripts/jquery.mmenu.min.all.js', array( 'jquery' ), null, true );
  wp_enqueue_script( 'global-js', get_template_directory_uri().'/javascripts/global.js', array( 'jquery', 'mmenu-js' ), null, true );
}

add_action("init", "create_news_post_type");
function create_news_post_type()
{
	register_post_type("newspost",
		array(
			"labels" 		=> array(
				"name" 			=> __("News"),
				"singular_name" => __("News"),
				"menu_name"		=> __("News"),
				),
			"public" 		=> true,
			"has_archive" 	=> false,
			"supports" 		=> array("title","thumbnail","editor"),
			"rewrite" 		=> array("slug" => "newpost"),
			)
		);
}


function pagination($pages = '', $range = 4)
{  
     $showitems = ($range * 2)+1;  
 
     global $paged;
     if(empty($paged)) $paged = 1;
 
     if($pages == '')
     {
         global $wp_query;
         $pages = $wp_query->max_num_pages;
         if(!$pages)
         {
             $pages = 1;
         }
     }   
 
     if(1 != $pages)
     {
         echo "<div class=\"pagination\"><span class=\"count\">Page ".$paged." of ".$pages."</span>";
         if($paged > 2 && $paged > $range+1 && $showitems < $pages) echo "<a href='".get_pagenum_link(1)."'>&laquo; First</a>";
         if($paged > 1 && $showitems < $pages) echo "<a href='".get_pagenum_link($paged - 1)."'>&lsaquo; Previous</a>";
 
         for ($i=1; $i <= $pages; $i++)
         {
             if (1 != $pages &&( !($i >= $paged+$range+1 || $i <= $paged-$range-1) || $pages <= $showitems ))
             {
                 echo ($paged == $i)? "<span class=\"current\">".$i."</span>":"<a href='".get_pagenum_link($i)."' class=\"inactive\">".$i."</a>";
             }
         }
 
         if ($paged < $pages && $showitems < $pages) echo "<a href=\"".get_pagenum_link($paged + 1)."\">Next &rsaquo;</a>";  
         if ($paged < $pages-1 &&  $paged+$range-1 < $pages && $showitems < $pages) echo "<a href='".get_pagenum_link($pages)."'>Last &raquo;</a>";
         echo "</div>\n";
     }
}

add_filter('widget_text','do_shortcode');


/* Changed excerpt length to 350 words*/
function my_excerpt_length($length) {
return 350;
}
add_filter('excerpt_length', 'my_excerpt_length');


function remove_vc_from_excerpt( $excerpt ) {
  return preg_replace( "/\[[\/]?vc_[^\]]*\]/", "", $excerpt );
}
add_filter( 'the_excerpt', 'remove_vc_from_excerpt' );

// ACF Display Custom Fields
add_filter( 'acf/settings/remove_wp_meta_box', '__return_false' );


