$(document).ready(function() {
    $("#button-confirm").click(function() {
        addPost();
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


});



function addPost() {
    var postTitle = $('.title-input').val();
    var postText = $('.message-input').val();
    var postAuthor = $('.author-input').val();

    var newPost = { post_title: postTitle, post_text: postText, post_author: postAuthor }

    $.post("/billboardapp/addpost", newPost, function(result) {
        Console.log(result)
    });
};