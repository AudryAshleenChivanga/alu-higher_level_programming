// Ensure the DOM is fully loaded before executing the script
$(document).ready(function() {
    // Use jQuery's get method to fetch data from the provided URL
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
        // Set the value of 'hello' from the response to the DIV#hello
        $('#hello').text(data.hello);
    });
});
