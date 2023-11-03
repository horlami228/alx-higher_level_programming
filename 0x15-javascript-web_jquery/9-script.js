$(function () {
    $.ajax({
        type: "GET",
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        success: function(data, status, check) {
            $('#hello').text(data['hello']);
            console.log(check.status);   
        }
    });
});
