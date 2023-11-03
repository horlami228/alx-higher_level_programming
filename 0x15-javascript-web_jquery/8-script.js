const $MovieList = $('#list_movies');

$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: 'json',
    success: function (data) {
        const $result = data.results;
        $.each($result, function (i, movie) {
            $MovieList.append("<li> " + movie['title'] + "</li>");
        });
    }
});