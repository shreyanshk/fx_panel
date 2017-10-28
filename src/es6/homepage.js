const fillColorObj = {
    safe:"#00ff00",
    caution:"#ffff00",
    danger:"#FF0000"
};

const stateId = {
  "Andaman and Nicobar Islands": "IN-AN",
  "Andhra Pradesh": "IN-AP",
  "Arunachal Pradesh": "IN-AR",
  "Assam": "IN-AS",
  "Bihar": "IN-BR",
  "Chandigarh": "IN-CH",
  "Chhattisgarh": "IN-CT",
  "Daman and Diu": "IN-DD",
  "Delhi": "IN-DL",
  "Dadra and Nagar Haveli": "IN-DN",
  "Goa": "IN-GA",
  "Gujarat": "IN-GJ",
  "Himachal Pradesh": "IN-HP",
  "Haryana": "IN-HR",
  "Jharkhand": "IN-JH",
  "Jammu and Kashmir": "IN-JK",
  "Karnataka": "IN-KA",
  "Kerala": "IN-KL",
  "Lakshadweep": "IN-LD",
  "Maharashtra": "IN-MH",
  "Meghalaya": "IN-ML",
  "Manipur": "IN-MN",
  "Madhya Pradesh": "IN-MP",
  "Mizoram": "IN-MZ",
  "Nagaland": "IN-NL",
  "Odisha": "IN-OR",
  "Punjab": "IN-PB",
  "Puducherry": "IN-PY",
  "Rajasthan": "IN-RJ",
  "Sikkim": "IN-SK",
  "Telangana": "IN-TG",
  "Tamil Nadu": "IN-TN",
  "Tripura": "IN-TR",
  "Uttar Pradesh":"IN-UP",
  "Uttarakhand": "IN-UT",
  "West Bengal": "IN-WB"
};

function updateMap(stateObj) {
    console.log("updating map with object");
    console.log(stateObj);
    for (let state in stateObj) {
        let fillColor;
        let numOfGun = 0;
        numOfGun = stateObj[state]["num_of_guns"];
        if (numOfGun<2) {
            fillColor = fillColorObj["safe"];
        } else if (numOfGun<5) {
            fillColor = fillColorObj["caution"];
        } else {
            fillColor = fillColorObj["danger"];
        }
        $('#'+stateId[state]).css("fill",fillColor);
    }
}

function getPastHourData() {
    console.log("getting past hour data");
    $.getJSON("/static/dummy.json", function(response) {
        console.log(response);
        updateMap(response);
    });
}

$(document).ready(
    function () {
        console.log("ready");
        getPastHourData();
    }
);
