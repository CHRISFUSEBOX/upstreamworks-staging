<?php
/**
 * The template for displaying all pages
 *
 * This is the template that displays all pages by default.
 * Please note that this is the WordPress construct of pages and that other
 * 'pages' on your WordPress site will use a different template.
 *
 * @package WordPress
 * @subpackage Twenty_Thirteen
 * @since Custom Theme 1.0
 */

get_header(); the_post(); ?>
    <!-- BEGIN: banner wrapper -->
    <section id="bannerWrapper">
    	
		<!-- BEGIN: shortbanner area -->
		<?php if(have_rows('banner', 82803)): while(have_rows('banner', 82803)): the_row();?>
		<?php $image = get_sub_field('banner_image'); ?>
		<article class="shortbannerArea"<?php if ( $image && isset( $image['url'] ) ) : ?> style="background-image: url(<?php echo $image['url']; ?>);"<?php endif; ?>>

		</article>
		<!-- END: shortbanner area -->
        <?php endwhile; endif; ?>  
    </section>
    <!-- END: banner wrapper -->
	
    <!-- BEGIN: middle wrapper -->
    <section id="middleWrapper">
		
		<!-- BEGIN: content area -->
        <article class="contentArea">
        	<div class="container">
			<?php if(have_rows('banner')): while(have_rows('banner')): the_row();?>
				<h1><?php the_sub_field('banner_title'); ?></h1>
				<p><?php the_sub_field('banner_description'); ?></p>
			<?php endwhile; endif; ?>  
				
				<?php the_content(); ?>
            </div>
        </article>
        <!-- END: content area -->
		
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