<?php
/**
 * The template for displaying Archive pages
 *
 * Used to display archive-type pages if nothing more specific matches a query.
 * For example, puts together date-based pages if no date.php file exists.
 *
 * If you'd like to further customize these archive views, you may create a
 * new template file for each specific one. For example, Custom Theme
 * already has tag.php for Tag archives, category.php for Category archives,
 * and author.php for Author archives.
 *
 * @link https://codex.wordpress.org/Template_Hierarchy
 *
 * @package WordPress
 * @subpackage Twenty_Thirteen
 * @since Custom Theme 1.0
 */

get_header(); ?>

    <!-- BEGIN: banner wrapper -->
    <section id="bannerWrapper">
    	
		<!-- BEGIN: shortbanner area -->
		<?php if(have_rows('banner',get_option( 'page_for_posts' ))): while(have_rows('banner',get_option( 'page_for_posts' ))): the_row();?>
		<?php $image = get_sub_field('banner_image'); ?>
		<article class="shortbannerArea" style="background-image: url(<?php echo $image['url']; ?>);">
			
		</article>
		<!-- END: shortbanner area -->
        <?php endwhile; wp_reset_query(); endif; ?>
		
    </section>
    <!-- END: banner wrapper -->
	
	    <!-- BEGIN: middle wrapper -->
    <section id="middleWrapper">
		
		<!-- BEGIN: news area -->
        <article class="newsArea">
        	<div class="container">
			
            <?php
			if(have_rows('banner',get_option( 'page_for_posts' ))): while(have_rows('banner',get_option( 'page_for_posts' ))): the_row();?>
				<h2><?php single_cat_title(); ?></h2>
				<p class="short"></p>
			<?php endwhile;  wp_reset_query(); endif; ?>
			
	    	<?php if ( is_category() ) { 
	    	$category = get_category( get_query_var( 'cat' ) );
            $cat_id = $category->cat_ID;
            if ($cat_id == 10 || $cat_id == 242 || $cat_id == 243 ) {
	    	?>
				<div class="blog-menu">
				    <?php dynamic_sidebar( 'blog' ); ?>
				</div>
			<?php } }?>
				
				<div class="news">
                    
                    <?php 
					
					if(have_posts()): while(have_posts()): the_post(); ?>
				        <?php
							// Retrieve the categories for the current post
							$categories = get_the_category(get_the_id());
							
							// Initialize category color variables
							$default_color = '#141d22';
							$category_color = '';
							$border = '';
							
							// Check if there are any categories
							if ($categories) {
								// Check if the post has only one category (parent category)
								if (count($categories) == 1) {
									// Get the color custom field value of the parent category
									$parent_category_color = get_field('category_color', 'category_' . $categories[0]->term_id);
									if ($parent_category_color) {
										$category_color = $parent_category_color;
									} else {
										// Fallback to default color if no color is specified for the parent category
										$category_color = $default_color;
									}
								} else {
									// Loop through each category to determine parent and subcategories
									$sub_category = null;
									foreach ($categories as $category) {
										if ($category->parent == 0) {
											// This is the parent category
											$parent_category = $category;
										} else {
											// This is a subcategory
											$sub_category = $category;
										}
									}

									// Check if the subcategory has a color assigned
									$sub_category_color = ( ! is_null( $sub_category ) ) ? get_field('category_color', 'category_' . $sub_category->term_id) : null;
									if ($sub_category_color) {
										$category_color = $sub_category_color;
									} else {
										// If no color is specified for the subcategory, use the parent category's color
										$parent_category_color = get_field('category_color', 'category_' . $parent_category->term_id);


										if ($parent_category_color) {
											$category_color = $parent_category_color;
										} else {
											// Fallback to default color if no color is specified for the parent category
											$category_color = $default_color;
										}
									}
								}
							}
							
							// If a color is found, set border style
							if ($category_color && $category_color !='#141d22') {
								$border = "style='border-left: 14px solid $category_color;'";
							}
						?>
						<div class="sub" <?php echo $border; ?>>
						
							<aside class="image col-xs-12 col-sm-4 col-md-3 col-lg-3">
								<?php the_post_thumbnail(); ?>
							</aside>
							
							<aside class="text col-xs-12 col-sm-8 col-md-9 col-lg-9">
								
								<div class="cat-and-date">
								    <?php
									// Check if there are categories assigned to the post
									if ( $categories ) {
										// Loop through each category
										foreach ( $categories as $term ) {
											// Check if the category is a parent category
											if ( $term->parent != 0 ) {
												// Assign the subcategory title
												$category_title = $term->name;
												break; // Exit the loop after finding the first subcategory
											} else {
												// Assign the parent category title
												$category_title = $term->name;
											}
										}
									}
									?>
									<span class="cat-name">
            							<?php echo $category_title; ?>
            						</span>
            						<span>|</span>
									<?php
    								$source = get_field('date');
    							    if ( $source ) {
    							    $date = new DateTime($source);
    							    ?>
    							    <span class="post-date">
    							        <?php echo $date->format('F j, Y'); ?>
    								</span>
    								<?php } ?>
								</div>
								<h3><?php the_title(); ?></h3>
								<p><?php 
								$content = strip_tags( do_shortcode( get_the_content() ) );
								echo wp_trim_words( $content, 40, '...' ); 
								?></p>
								<?php
								    $link = get_field( 'post_link' );
								    if ( $link ) {
								?>
								    <a href="<?php echo $link; ?>" class="more" target="_blank">Read more <i class="fa fa-external-link"></i></a>
								<?php } else { ?>
								    <a href="<?php echo get_permalink(); ?>" class="more"><?php _e('Read more');?></a>
								<?php } ?>
								
							</aside>
					
						</div>
					<?php endwhile; endif; ?>
					
				</div>
				
				<div class="newspageing">
					
					<?php if ( function_exists( 'pagination' ) ) { pagination( $GLOBALS['wp_query']->max_num_pages ); } ?>
				
				</div>
				
            </div>
        </article>
        <!-- END: news area -->
		
		<!-- BEGIN: case area -->
		<article class="caseArea">
			<div class="container">
				<div class="row">
					<?php if(have_rows('blog_list')): $sNo=0; while(have_rows('blog_list')): the_row(); $sNo++;
					 switch ($sNo) {
						case 1:
							$class ='blog';
							break;
						case 2:
							$class ='';
							break;
						case 3:
							$class ='event';
							break;
						
					} 
					?>
					 <aside onclick="location.href='<?php the_sub_field('blog_link'); ?>'" class="case <?php echo $class; ?> col-xs-12 col-sm-4 col-md-4 col-lg-4">
						
						<h3><?php the_sub_field('blog_title'); ?></h3>
						<?php the_sub_field('blog_description'); ?>
						<?php if(get_sub_field('blog_image')): ?>
							<img src="<?php the_sub_field('blog_image'); ?>" alt="<?php the_sub_field('blog_title'); ?>" />
						<?php endif; ?>
					 </aside>
					<?php endwhile; endif; ?>
				
				</div>
			</div>
		</article>
		<!-- END: case area -->	
				
    </section>
    <!-- END: middle wrapper -->

<?php get_footer(); ?>