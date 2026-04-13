<?php
/**
 * The template for displaying the footer
 *
 * Contains footer content and the closing of the #main and #page div elements.
 *
 * @package WordPress
 * @subpackage Twenty_Thirteen
 * @since Custom Theme 1.0
 */
?>
    <!-- BEGIN: footer wrapper -->
    <footer id="footerWrapper">
    	<div class="container">
		
        <!-- BEGIN: footer area -->
        <div class="footerArea">
			
			<?php dynamic_sidebar('footermenu'); ?>
					 
        </div>
        <!-- BEGIN: footer area -->
        
        <!-- BEGIN: copyright area -->
        <div class="copyrightArea">
			
			<aside class="copyright">
			
				
<p>© <?php echo date('Y'); ?> Upstream Works All Rights Reserved.</p>


				
				<?php wp_nav_menu('menu=footermenu'); ?>
			
			</aside>
			
			<nav class="social">
				<ul>
					<li><a class="fa-brands fa-linkedin" target="_blank" href="<?php the_field('linkedin','options'); ?>"></a></li>
					
					<li><a class="fa-brands fa-square-facebook" target="_blank" href="<?php the_field('facebook','options'); ?>"></a></li>
					
                    <li><a class="fa-brands fa-square-bluesky" target="_blank" href="<?php the_field('bluesky','options'); ?>"></a></li>
				</ul>
			
			</nav>
       		
        </div>
        <!-- BEGIN: copyright area -->
		
		 </div> 
    </footer>
    <!-- END: footer wrapper -->
    
</div>
<!-- END: wrapper -->

 <?php wp_footer(); ?>
<!-- Netresults -->
<?php if ( ! defined('WP_ENV') || WP_ENV !== 'staging' ) : ?>
<script id="__maSrc" type="text/javascript" data-pid="18624"> (function(c,a,p,s) { p=c.createElement(a); p.type='text/java'+a; p.setAttribute('crossorigin', 'anonymous'); p.src='https://beacon.cdnma.com/apps/18624/capture.js'; s=c.getElementsByTagName(a)[0];s.parentNode.insertBefore(p,s); }(document,'script')); </script>
<?php endif; ?>
<!-- END: wrapper -->

 <script src="<?php echo get_template_directory_uri(); ?>/javascripts/eventsadj.js"></script> 	

<!-- Upstream Works Chat -->
<?php if ( ! defined('WP_ENV') || WP_ENV !== 'staging' ) : ?>
<script>

    (function(win, doc, s, host, file, ts, obj, id, elem, sib) {
        win[obj] = win[obj] || (function() { (win[obj].queue = win[obj].queue || []).push(arguments); });
        elem = doc.createElement(s);
        elem.async = 1;
        elem.src = host + file + "?" + ts;
        elem.id = id;
        elem.setAttribute('data-host', host);
        sib = doc.getElementsByTagName(s)[0];
        sib.parentNode.insertBefore(elem, sib);
    })(window, document, 'script', 'https://custservice.uwd.upstreamworkssoftware.com', '/scripts/floatingChat.js', Math.round(new Date().getTime() / 1.44e6), '_uwc', '_uwc-tag');
  /*
    Use one command from below commands as User can fetch form either by url or by tagName
    _uwc('use-form', 'https://abc.com/chatform');
    _uwc('use-form', 'Default_1');
  */
  _uwc('check-availability', ['Chat']);

   _uwc('create', 1);

</script>
<?php endif; ?>
<!-- End Upstream Works Chat -->

</body>
</html>