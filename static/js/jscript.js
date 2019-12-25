$(document).on('submit', '#form_abonnement', function(e){
    e.preventDefault();
    $.ajax({
        type:'post',
        url:'create_abonne',
        data:{
            mail : $('#mail').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
            alert('bien fait');
        }
    });
});


