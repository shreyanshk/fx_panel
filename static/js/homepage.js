"use strict";

var fillColorObj = {
    safe: "#00ff00",
    caution: "#ffff00",
    danger: "#FF0000"
};

var stateId = {
    "AN": "IN-AN",
    "AP": "IN-AP",
    "AR": "IN-AR",
    "AS": "IN-AS",
    "BR": "IN-BR",
    "CH": "IN-CH",
    "CT": "IN-CT",
    "DD": "IN-DD",
    "DL": "IN-DL",
    "DN": "IN-DN",
    "GA": "IN-GA",
    "GJ": "IN-GJ",
    "HP": "IN-HP",
    "HR": "IN-HR",
    "JH": "IN-JH",
    "JK": "IN-JK",
    "KA": "IN-KA",
    "KL": "IN-KL",
    "LD": "IN-LD",
    "MH": "IN-MH",
    "ML": "IN-ML",
    "MN": "IN-MN",
    "MP": "IN-MP",
    "MZ": "IN-MZ",
    "NL": "IN-NL",
    "OR": "IN-OR",
    "PB": "IN-PB",
    "PY": "IN-PY",
    "RJ": "IN-RJ",
    "SK": "IN-SK",
    "TG": "IN-TG",
    "TN": "IN-TN",
    "TR": "IN-TR",
    "UP": "IN-UP",
    "UT": "IN-UT",
    "WB": "IN-WB"
};

function updateMap(stateObj) {
    console.log("updating map with object");
    console.log(stateObj);
    for (var state in stateObj) {
        var fillColor = void 0;
        var numOfGun = 0;
        numOfGun = stateObj[state];
        if (numOfGun < 700) {
            fillColor = fillColorObj["safe"];
        } else if (numOfGun < 900) {
            fillColor = fillColorObj["caution"];
        } else {
            fillColor = fillColorObj["danger"];
        }
        $('#' + stateId[state]).css("fill", fillColor);
    }
}

function getGunData(from,period,count) {
    console.log("getting past hour data");
    $.getJSON("http://localhost:5000/api/v1/get_arm_report_dummy",{"fromtime":1509212130,"period":1509212130,"count":1})
        .done( function (response) {
            console.log(response);
            updateMap(response[0]);
    });
}

$(document).ready(function () {
    console.log("ready");
    $("#day-btn").click(function () {
        var $input = $( this );
        $input.attr("autofocus","false");
        $input.addClass("active");
        $("#hour-btn").removeClass("active");
        $("#week-btn").removeClass("active");
    });
    $("#hour-btn").click(function () {
        var $input = $( this );
        $input.attr("autofocus","false");
        $input.addClass("active");
        $("#day-btn").removeClass("active");
        $("#week-btn").removeClass("active");
    });
    $("#week-btn").click(function () {
        var $input = $( this );
        $input.attr("autofocus","false");
        $input.addClass("active");
        $("#hour-btn").removeClass("active");
        $("#day-btn").removeClass("active");
    });
    var from = new Date().getTime();
    var period = 3600;
    var count = 1;
    getGunData(from,period,count);
});