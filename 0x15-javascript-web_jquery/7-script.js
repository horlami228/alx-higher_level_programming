$(function () {
    const $character = $('#character');

$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/people/3/?format=json",
    success: function (response) {
        $character.text(response.name);
    }
});
});
