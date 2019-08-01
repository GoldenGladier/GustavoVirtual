$( document ).ready(function() {

	$("p").addClass("6u 12u$(xsmall)");
	$("p:first").removeClass("6u 12u$(xsmall)");
	$("p").last().removeClass("6u 12u$(xsmall)");
	$("p").last().addClass("12u$");
	$("label").css('display', 'none');
	$("p").css('margin', '0');
	$("#id_contact_name").attr("placeholder", "Nombre");
	$("#id_contact_email").attr("placeholder", "Email");
	$("#id_content").attr("placeholder", "Mensaje");
	$("#id_content").css("height", "150px");
});