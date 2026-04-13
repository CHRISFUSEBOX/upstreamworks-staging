<!DOCTYPE html><!--[if IE 7]><html class="ie ie7" <?php language_attributes(); ?>><![endif]--><!--[if IE 8]><html class="ie ie8" <?php language_attributes(); ?>><![endif]--><!--[if !(IE 7) & !(IE 8)]><!--><html <?php language_attributes(); ?>><!--<![endif]--><head>	<meta charset="<?php bloginfo( 'charset' ); ?>"><meta name="viewport" content="width=device-width"><title><?php wp_title('&laquo;', true, 'right'); ?> <?php bloginfo('name'); ?></title><link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>"><!--[if lt IE 9]>	<script src="<?php echo get_template_directory_uri(); ?>/js/html5.js"></script>	<![endif]--><?php wp_head(); ?>  
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-610621116"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-610621116');
</script>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NRHX2X3');</script>
<!-- End Google Tag Manager -->


<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-42289123-1', 'auto');
  ga('send', 'pageview');

</script>

<script type="text/javascript" language="javascript">
      var sf14gv = 12243;
      (function() {
      var sf14g = document.createElement('script'); sf14g.type = 'text/javascript'; sf14g.async = true;
      sf14g.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 't.sf14g.com/sf14g.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sf14g, s);
      })();


<!-- Hotjar Tracking Code for https://www.upstreamworks.com/platforms/amazon-connect/watch-demo -->
<?php if ( ! defined('WP_ENV') || WP_ENV !== 'staging' ) : ?>
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:2442198,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>
<?php endif; ?>
	</script> 
<meta name="google-site-verification" content="30ycLKRe540zJvLx4VbB-OHC84yfD4YSgDLZtVvXKYo" />
<meta name="google-site-verification" content="y2MHLTGN0Awqnw9yHmzm0bPLh3S0IArEJWR_bFWpfZ8" />
 <script src="<?php echo get_template_directory_uri(); ?>/javascripts/cf7.js"></script> 
<script>
	window.SGPMPopupLoader=window.SGPMPopupLoader||{ids:[],popups:{},call:function(w,d,s,l,id){
		w['sgp']=w['sgp']||function(){(w['sgp'].q=w['sgp'].q||[]).push(arguments[0]);}; 
		var sg1=d.createElement(s),sg0=d.getElementsByTagName(s)[0];
		if(SGPMPopupLoader && SGPMPopupLoader.ids && SGPMPopupLoader.ids.length > 0){SGPMPopupLoader.ids.push(id); return;}
		SGPMPopupLoader.ids.push(id);
		sg1.onload = function(){SGPMPopup.openSGPMPopup();}; sg1.async=true; sg1.src=l;
		sg0.parentNode.insertBefore(sg1,sg0);
		return {};
	}};
	SGPMPopupLoader.call(window,document,'script','https://popupmaker.com/assets/lib/SGPMPopup.min.js','91441001');
</script>
</head>
<body <?php body_class(); ?>><!-- BEGIN: wrapper -->
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NRHX2X3"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<div id="wrapper"><!-- BEGIN: header wrapper -->    
<header id="headerWrapper">
<div class="container"><!-- BEGIN: logo area -->
	<nav class="logoArea">	<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><img src="<?php echo get_template_directory_uri(); ?>/images/logo.png" alt="<?php bloginfo( 'name' ); ?>" /></a></nav><!-- END: logo area --><!-- BEGIN: header right --><div class="headeRight"><!-- BEGIN: contact area --><nav class="contactArea"><?php wp_nav_menu('menu=topmenu'); ?></nav><!-- END: contact area --><!-- BEGIN: menu area --><nav class="menuArea"><?php wp_nav_menu('menu=mainmenu'); ?>	</nav><!-- END: menu area --><!-- BEGIN: mobilemenu area --><nav class="mobilemenuArea"><a class="menutoggle" href="#menu"><span></span><span></span><span></span></a><nav id="menu"><?php wp_nav_menu('menu=mobilemenu'); ?>	</nav>	</nav><!-- END: mobilemenu area -->	</div><!-- END: header right -->   </div>    </header>    <!-- END: header wrapper -->