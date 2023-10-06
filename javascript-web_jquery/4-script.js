// Use jQuery to listen for a click event on the DIV#toggle_header
$('#toggle_header').click(function() {
    // Toggle between 'red' and 'green' classes for the <header>
    if ($('header').hasClass('red')) {
        $('header').removeClass('red').addClass('green');
    } else {
        $('header').removeClass('green').addClass('red');
    }
});
