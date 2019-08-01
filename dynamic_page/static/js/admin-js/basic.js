var id = null;
var pathname = window.location.pathname;

$( document ).ready(function() {
    console.log( "ready!" );

    $(".boton").click(function(){
        id = ($(this).attr("id"));
        devuelveID();
    });

    var item =$('#id_typeClass').val();
    cambioDeClase(item);
});

$('#id_typeClass').change(function(){
    var item =$(this).val();
    cambioDeClase(item);
});

function cambioClaseDesdeImagen(item){
    cambioDeClase(item);
    cambioDeItem(item);
}

function cambioDeItem(item){
    if(item == 'txtsimple'){
        document.getElementById('id_typeClass').value = 'txtsimple'; 
    }
    else if(item == 'txtimg-left'){
        document.getElementById('id_typeClass').value = 'txtimg-left'; 
    }
    else if(item == 'txtimg-right'){
        document.getElementById('id_typeClass').value = 'txtimg-right'; 
    }
    else if(item == 'txtsimple-img'){
        document.getElementById('id_typeClass').value = 'txtsimple-img'; 
    }
}

function cambioDeClase(valorCambiado){
    $('#text-simple').css('box-shadow','none');
    $('#text-img-right').css('box-shadow','none');
    $('#text-img-left').css('box-shadow','none');
    $('#text-img-bottom').css('box-shadow','none');
    if(valorCambiado != 'txtsimple'){
        $('#save-home').css('margin-top','0px');
        $('label[for=id_image]').css('display','inline');

        if(valorCambiado == 'txtsimple'){
            $('#text-simple').css('box-shadow','0px 0px 30px #21c0ff');
        }
        else if(valorCambiado == 'txtimg-left'){
            $('#text-img-left').css('box-shadow','0px 0px 30px #21c0ff');
        }
        else if(valorCambiado == 'txtimg-right'){
            $('#text-img-right').css('box-shadow','0px 0px 30px #21c0ff');
        }
        else if(valorCambiado == 'txtsimple-img'){
            $('#text-img-bottom').css('box-shadow','0px 0px 30px #21c0ff');
        }
        else{
            console.log("Error al seleccionar algo...")
        }
    }
    else{
        $('#text-simple').css('box-shadow','0px 0px 30px #21c0ff');
        $('#save-home').css('margin-top','46px');
        $('label[for=id_image]').css('display','none');
    }
}

function devuelveID(){
    var form = document.getElementById('form-modal') || null;
    if(form) {
    form.action = pathname + '/' + id + "/delete/"
    }
    // EXAMPLE LINK ===> http://127.0.0.1:8000/Gustavo_Virtual/AdminMaster/home-articles-list/35/delete/
}

var active = false;
function animateMenu(){
    if(active == false){
       $('.menu_Mobile').animate({
            left: '0%'
        });
        active = true;
    }
    else{
        $('.menu_Mobile').animate({
            left: '-100%'
        });
        active = false;
    }
}

$(window).resize(function(){
    var ancho = screen.width;
    if (ancho > 809){
        $('.menu_Mobile').animate({
            left: '-100%'
        });
        active = false;
    }
})

$('label[for=id_studyPlan]').css('display','inline');
$('label[for=id_studyPlan]').html('<i class="fas fa-file-upload"></i> Plan de Estudio'); 
$('label[for=id_studyPlan]').toggleClass('boton btn-upload');

$('label[for=id_image]').css('display','inline-block');
$('label[for=id_image]').html('<i class="fas fa-file-upload"></i> Imagen'); 
$('label[for=id_image]').toggleClass('boton btn-upload');

$('#id_studyPlan').css('display','none');
$('#studyPlan-clear_id').css('display','none');

$('#id_resource').css('display','none');
$('label[for=id_resource]').css('display','inline-block');
$('label[for=id_resource]').html('<i class="fas fa-file-upload"></i> Documento'); 
$('label[for=id_resource]').toggleClass('boton btn-upload');
$('label[for=id_resource]').css('display','inline');

$('#id_avatar').css('display','none');
$('label[for=id_avatar]').css('display','inline-block');
$('label[for=id_avatar]').html('<i class="fas fa-file-upload"></i> Foto'); 
$('label[for=id_avatar]').toggleClass('boton btn-upload');
$('label[for=id_avatar]').css('display','inline');

$('label[for=avatar-clear_id]').css('display','none');
$('#avatar-clear_id').css('display','none');

//$("form > p:last").css('display','none');
