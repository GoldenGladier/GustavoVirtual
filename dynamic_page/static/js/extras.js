$( document ).ready(function() {
    console.log( "ready!" );

    $(window).load(function() {
        $("#preloader").fadeOut("slow");
    }); 

    $("#close").click(function(){
        setTimeout(
            function(){
                $("#noti").addClass( "disabled" );
            }, 1000);
    });

    // $('body').css('background-image', "url('/static/images/log/fondo.webp')");    
    Reloj();
});

function Reloj(){
    var tiempo = new Date();
    console.log(tiempo.getHours() + ':' + tiempo.getMinutes());
    if(tiempo.getHours() > 3 && tiempo.getHours() < 6){
        $("body").css("background-image", "url('/static/images/log/6.webp')");
        }
    else if(tiempo.getHours() >= 6 && tiempo.getHours() < 10){
        $("body").css("background-image", "url('/static/images/log/1.webp')");
        }
    else if(tiempo.getHours() >= 10 && tiempo.getHours() < 16){
        $("body").css("background-image", "url('/static/images/log/2.webp')");
        }
    else if(tiempo.getHours() >= 16 && tiempo.getHours() < 20){
        $("body").css("background-image", "url('/static/images/log/3.webp')");
        }
    else if(tiempo.getHours() >= 20 && tiempo.getHours() < 22){
        $("body").css("background-image", "url('/static/images/log/5.webp')");
        }
    else if(tiempo.getHours() >= 22){
        $("body").css("background-image", "url('/static/images/log/4.webp')");
        }
    else if(tiempo.getHours() >= 0 && tiempo.getHours() <=3 ){
        $("body").css("background-image", "url('/static/images/log/4.webp')");
        }
    else{
        $("body").css("background-image", "url('/static/images/log/form.webp')");
        console.log("Error al establecer ambientación de acuerdo al horario.")
    }
    // url('../images/log/2.webp');
}
