'use strict';

$(document).ready(function () {
    $('input[type=radio][name=userTypeRadio]').change(function () {
        if (this.value == 'New') {
            $('.new-user').css("display", "block");
        } else if (this.value == 'Registered') {
            $('.new-user').css("display", "none");
        }
    });
});