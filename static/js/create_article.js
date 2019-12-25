$(document).on('submit', '#form_new_article', function(e){
    e.preventDefault();

    console.log(typeof($('#sendable').val()));
    console.log($('#state').val());
    console.log($('#categorie').val());
    $.ajax({
        type:'post',
        url:'create_article',
        data:{
            user : $('#user').val(),
            title : $('#title').val(),
            content : $('#content').val(),
            category : $('#categor').val(),
            image : $('#avant_plan').val(),
            state : $('#state').val(),
            sendable : $('#sendable').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]')
        },
        success: function(){
            alert('article créé');
        }
    });
});
