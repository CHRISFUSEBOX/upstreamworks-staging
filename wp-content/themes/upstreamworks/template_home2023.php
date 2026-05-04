<?php
/**
 * Template Name: Home2023
 */
get_header(); the_post(); ?>
	<!-- BEGIN: banner wrapper -->
    <section id="bannerWrapper">
	</section>
	<!-- END: banner wrapper -->	
	
	<!-- BEGIN: middle wrapper -->  
	<section id="middleWrapper">  

	<?php the_content(); ?>
	
	<?php if (get_field('boxes') == "Yes") { ?>
	<!-- BEGIN: case area -->
	<article class="caseArea">
		<div class="container">
			<div class="row">
				<?php include_once("casearea.php"); ?>
			
			</div>
		</div>
	</article>
	<!-- END: case area -->	
	<?php } //end conditional boxes ?>  

	
	
	</section>   
	<!-- END: middle wrapper -->
	
<?php get_footer(); ?>
	
	