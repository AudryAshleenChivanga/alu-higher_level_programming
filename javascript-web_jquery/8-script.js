// Use jQuery's get method to fetch data from the provided URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Loop through each movie in the received data
    data.results.forEach(function(movie) {
        // Append the movie title as a new list item to the UL#list_movies
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
