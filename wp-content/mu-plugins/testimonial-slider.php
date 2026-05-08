<?php
add_action( 'wp_footer', function() {
	if ( ! is_front_page() ) return;
	?>
	<script>
	(function(){
		function init(){
			var section=document.querySelector('.vc_custom_1060');
			if(!section)return;
			var cols=Array.from(section.querySelectorAll('.vc_row.vc_inner [class*="vc_col"]'));
			var testimonials=cols.filter(function(c){return c.querySelector('blockquote');});
			if(testimonials.length<2)return;
			var data=testimonials.map(function(col){
				var img=col.querySelector('img');
				var quote=col.querySelector('blockquote p');
				var name=col.querySelector('strong');
				var role=col.querySelector('em');
				return{
					photo:img?(img.getAttribute('data-lazy-src')||img.getAttribute('src')):'',
					quote:quote?quote.innerHTML:'',
					name:name?name.textContent.replace(/^[—\-]\s*/,'').replace(/,\s*$/,'').trim():'',
					role:role?role.textContent.trim():''
				};
			});
			Array.from(section.querySelectorAll('.vc_row.vc_inner')).forEach(function(r){r.style.display='none';});
			var slider=document.createElement('div');slider.className='usw-testimonial-slider';
			data.forEach(function(t,i){
				var slide=document.createElement('div');
				slide.className='usw-testimonial-slide'+(i===0?' usw-active':'');
				slide.innerHTML='<span class="usw-quote-mark">“</span>'
					+'<blockquote><p>'+t.quote+'</p></blockquote>'
					+'<div class="usw-person">'
					+(t.photo?'<img src="'+t.photo+'" alt="'+t.name+'" loading="lazy">':'')
					+'<div class="usw-person-info">'
					+'<div class="usw-person-name">'+t.name+'</div>'
					+'<div class="usw-person-role">'+t.role+'</div>'
					+'</div></div>';
				slider.appendChild(slide);
			});
			var prevBtn=document.createElement('button');
			prevBtn.className='usw-slider-btn usw-slider-prev';
			prevBtn.innerHTML='&#8249;';
			var nextBtn=document.createElement('button');
			nextBtn.className='usw-slider-btn usw-slider-next';
			nextBtn.innerHTML='&#8250;';
			var dotsEl=document.createElement('div');
			dotsEl.className='usw-slider-dots';
			data.forEach(function(_,i){
				var dot=document.createElement('button');
				dot.className='usw-slider-dot'+(i===0?' usw-active':'');
				dotsEl.appendChild(dot);
			});
			slider.appendChild(prevBtn);slider.appendChild(nextBtn);slider.appendChild(dotsEl);
			var innerRows=Array.from(section.querySelectorAll('.vc_row.vc_inner'));
			var lastRow=innerRows[innerRows.length-1];
			lastRow.parentNode.insertBefore(slider,lastRow.nextSibling);
			var slides=slider.querySelectorAll('.usw-testimonial-slide');
			var dots=dotsEl.querySelectorAll('.usw-slider-dot');
			var current=0,autoplay;
			function goTo(n){
				slides[current].classList.remove('usw-active');dots[current].classList.remove('usw-active');
				current=((n%slides.length)+slides.length)%slides.length;
				slides[current].classList.add('usw-active');dots[current].classList.add('usw-active');
			}
			function start(){autoplay=setInterval(function(){goTo(current+1);},6000);}
			prevBtn.addEventListener('click',function(){goTo(current-1);});
			nextBtn.addEventListener('click',function(){goTo(current+1);});
			dots.forEach(function(d,i){d.addEventListener('click',function(){goTo(i);});});
			slider.addEventListener('mouseenter',function(){clearInterval(autoplay);});
			slider.addEventListener('mouseleave',start);
			start();
		}
		if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init);}else{init();}
	})();
	</script>
	<?php
}, 9999 );
