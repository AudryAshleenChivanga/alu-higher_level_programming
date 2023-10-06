// Use jQuery to listen for a click event on the DIV#add_item
$('#add_item').click(function() {
    // Append a new <li> element to the UL.my_list
    $('.my_list').append('<li>Item</li>');
});
