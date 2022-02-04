window.setTimeout(function() {
    if($('.alert').is(":visible")){
        $('.alert').fadeTo(500, 0).slideUp(500,
            function(){
                $(this).remove();
            });
    }
}, 4000)

function baixaTxt() {
    var resultado = document.querySelectorAll("#resultado")[0]
    var data = new Blob(resultado)

    if(resultado == null){
        
    }
}