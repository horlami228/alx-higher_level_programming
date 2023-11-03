const $ToggleHeader = $('#toggle_header');
$ToggleHeader.on('click', function () {
    $('header').toggleClass('red green');
});
