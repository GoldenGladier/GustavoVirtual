/*
	Retrospect by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

(function($) {

	skel
		.breakpoints({
			xlarge: '(max-width: 1680px)',
			large: '(max-width: 1280px)',
			medium: '(max-width: 980px)',
			small: '(max-width: 736px)',
			xsmall: '(max-width: 480px)'
		});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

			
		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

		// Nav.
			$('#nav')
				.append('<a href="#nav" class="close"></a>')
				.appendTo($body)
				.panel({
					delay: 500,
					hideOnClick: true,
					hideOnSwipe: true,
					resetScroll: true,
					resetForms: true,
					side: 'right'
				});

	});

})(jQuery);

$( document ).ready(function() {
    $(window).load(function() {
        $("#preloader").fadeOut("slow");
	}); 
	
	// $("p").addClass("6u 12u$(xsmall)");
	// $("p:first").removeClass("6u 12u$(xsmall)");
	// $("p").last().removeClass("6u 12u$(xsmall)");
	// $("p").last().addClass("12u$");
	// $("label").css('display', 'none');
	// $("p").css('margin', '0');
	// $("#id_contact_name").attr("placeholder", "Nombre");
	// $("#id_contact_email").attr("placeholder", "Email");
	// $("#id_content").attr("placeholder", "Mensaje");
	// $("#id_content").css("height", "150px");
});