<?php
/**
 * The template for displaying all single posts
 *
 * @package WordPress
 * @subpackage Twenty_Thirteen
 * @since Custom Theme 1.0
 */

get_header(); ?>

 <!-- BEGIN: banner wrapper -->
    <section id="bannerWrapper">
    	
		<!-- BEGIN: shortbanner area -->
		<?php if(have_rows('banner', 82803)): while(have_rows('banner', 82803)): the_row();?>
		<?php $image = get_sub_field('banner_image'); ?>
		<article class="shortbannerArea"<?php if ( $image && isset( $image['url'] ) ) : ?> style="background-image: url(<?php echo esc_url( $image['url'] ); ?>);"<?php endif; ?>>

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
				
				<?php if (have_posts()) : ?>

					<?php while (have_posts()) : the_post(); ?>
					
						<h3><?php the_title(); ?></h3>
						<p><?php the_content(); ?></p>
				

					<?php endwhile; ?>

				<?php endif; ?>

            
			</div>
        </article>
        <!-- END: content area -->				
		
    </section>
    <!-- END: middle wrapper -->
	
<?php get_footer(); ?>