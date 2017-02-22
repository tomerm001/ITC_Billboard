$(document).ready(function() {

    // prevent form from refreshing by removing default and creating manual ajax post
    $('#new-post-form').submit(function(e) {
        $.post('/billboardapp/addpost', $(this).serialize(), function(data){
            console.log(data.message);
        });
        e.preventDefault();
    });

    // Attache actions to button
    $("#button-confirm").click(function() {
        
        // post form
        $('#new-post-form').submit();
 
        $('#confirm-message-container').slideUp();
        $('#input-container').slideUp();
        $('#addmessage-container').slideDown();
        location.reload();
    });

    // hide input and confirm cells
    $('#input-container').hide();
    $('#confirm-message-container').hide();

    // add event listener to add message
    $("#button-add").click(function() {
        $('#input-container').slideDown();
        $('#confirm-message-container').slideDown();
        $('#addmessage-container').hide();
    });

    // add event listener to cancel input
    $('#button-cancel').click(function() {
        $('#confirm-message-container').slideUp();
        $('#input-container').slideUp();
        $('#addmessage-container').slideDown();
    })

    // add event listener to delete button
    $('.delete-container').css( 'cursor', 'pointer' );
    $(".delete-container").click(function(){
        var postId = $(this).attr("alt");
        deletePost(postId);
    });
});


// delete a specific post
function deletePost(postId){
    console.log(postId);
    
    $.post( '/billboardapp/delpost', { postid: postId }, function( data ) {
            console.log("complete");
        }, "json");

    location.reload();


};