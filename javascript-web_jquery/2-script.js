// I am using jQuery to listen for a click event on the DIV#red_header
$('#red_header').click(function() {
    // When clicked, change the text color of the <header> to red (#FF0000)
    $('header').css('color', '#FF0000');
});
