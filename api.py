import json

from flask import Blueprint, request
from random import randint

from models.dbmodels import session, FirearmTxn

view = Blueprint('api', __name__)
statedict = {
	"AP": 0,
	"AR": 0,
	"AS": 0,
	"BR": 0,
	"CG": 0,
	"GA": 0,
	"GJ": 0,
	"HR": 0,
	"HP": 0,
	"JK": 0,
	"JH": 0,
	"KA": 0,
	"KL": 0,
	"MP": 0,
	"MH": 0,
	"MN": 0,
	"ML": 0,
	"MZ": 0,
	"NL": 0,
	"OR": 0,
	"PB": 0,
	"RJ": 0,
	"UT": 0,
	"CT": 0,
	"TG": 0,
	"SK": 0,
	"TN": 0,
	"TR": 0,
	"UK": 0,
	"UP": 0,
	"WB": 0,
	"AN": 0,
	"CH": 0,
	"DH": 0,
	"DD": 0,
	"DL": 0,
	"LD": 0,
	"PY": 0,
}


@view.route("/api/v1/get_arm_report", methods=["GET"])
def get_arm_report():
	data = request.args
	try:
		fromtime = int(data['fromtime'])
		period = int(data['period'])
		count = int(data['count'])
	except KeyError:
		return "", 404
	totime = fromtime + period*count
	vals = []
	slots = [(i, i+period) for i in range(fromtime, totime, period)]
	for slot in slots:
		res = session.query(FirearmTxn).filterby(
			FirearmTxn.date >= slot[0],
			FirearmTxn.data < slot[1],
		).all().count()
		vals.append(res)
	return json.dumps(vals)


@view.route("/api/v1/get_arm_report_dummy", methods=["GET"])
def return_dummy_get_arm_report():
	data = request.args
	try:
		fromtime = int(data['fromtime'])
		period = int(data['period'])
		count = int(data['count'])
	except KeyError:
		return "", 404
	retarr = []
	for _ in range(count):
		newdict = dict(statedict)
		for key in newdict.keys():
			newdict[key] = randint(0, 1000)
		retarr.append(newdict)
	return json.dumps(retarr)


@view.route("/api/v1/dummy_get_crime_report")
def return_dummy_crime_data():
	data = [
		{
			"AN": 34,
			"AP": 16477,
			"AR": 180,
			"AS": 4243,
			"BR": 5356,
			"CH": 150,
			"CT": 3989,
			"DN": 19,
			"DD": 10,
			"DL": 2291,
			"GA": 83,
			"GJ": 5805,
			"HR": 3393,
			"HP": 890,
			"JK": 1656,
			"JH": 2229,
			"KA": 6002,
			"KL": 5450,
			"LD": 0,
			"MP": 14549,
			"MH": 12524,
			"MN": 112,
			"ML": 66,
			"MZ": 126,
			"NL": 30,
			"OR": 5357,
			"PY": 119,
			"PB": 2361,
			"RJ": 12175,
			"SK": 24,
			"TN": 10111,
			"TR": 438,
			"UP": 20227,
			"UT": 749,
			"WB": 6570,
		},
		{
			"AP": 18880,
			"AR": 159,
			"AS": 5092,
			"BR": 5743,
			"CH": 189,
			"CT": 3538,
			"DN": 15,
			"DD": 8,
			"DL": 2216,
			"GA": 76,
			"GJ": 5373,
			"HR": 4385,
			"HP": 838,
			"JK": 2016,
			"JH": 2490,
			"KA": 6170,
			"KL": 5829,
			"LD": 2,
			"MP": 15260,
			"MH": 11322,
			"MN": 170,
			"ML": 71,
			"MZ": 154,
			"NL": 26,
			"OR": 4779,
			"PY": 141,
			"PB": 2295,
			"RJ": 12049,
			"SK": 28,
			"TN": 9798,
			"TR": 536,
			"UP": 15647,
			"UT": 870,
			"WB": 6842,
		},
		{
			"AP": 18382,
			"AR": 139,
			"AS": 5312,
			"BR": 5900,
			"CH": 159,
			"CT": 3336,
			"DN": 13,
			"DD": 10,
			"DL": 3282,
			"GA": 121,
			"GJ": 5735,
			"HR": 4170,
			"HP": 729,
			"JK": 2164,
			"JH": 2488,
			"KA": 5834,
			"KL": 5653,
			"LD": 4,
			"MP": 14547,
			"MH": 11273,
			"MN": 137,
			"ML": 69,
			"MZ": 147,
			"NL": 25,
			"OR": 4946,
			"PY": 121,
			"PB": 2375,
			"RJ": 11812,
			"SK": 37,
			"TN": 8888,
			"TR": 537,
			"UP": 12840,
			"UT": 886,
			"WB": 8508
		},
		{
			"AP": 18921,
			"AR": 148,
			"AS": 5700,
			"BR": 8091,
			"CH": 188,
			"CT": 3763,
			"DN": 22,
			"DD": 7,
			"DL": 3677,
			"GA": 132,
			"GJ": 6211,
			"HR": 4276,
			"HP": 823,
			"JK": 2208,
			"JH": 2490,
			"KA": 5423,
			"KL": 6483,
			"LD": 1,
			"MP": 15203,
			"MH": 12169,
			"MN": 134,
			"ML": 113,
			"MZ": 91,
			"NL": 30,
			"OR": 5239,
			"PY": 110,
			"PB": 1955,
			"RJ": 13127,
			"SK": 49,
			"TN": 9332,
			"TR": 670,
			"UP": 15485,
			"UT": 988,
			"WB": 11047,
		},
		{
			"AP": 20819,
			"AR": 150,
			"AS": 6027,
			"BR": 6019,
			"CH": 205,
			"CT": 3599,
			"DN": 24,
			"DD": 10,
			"DL": 4351,
			"GA": 121,
			"GJ": 6343,
			"HR": 4161,
			"HP": 793,
			"JK": 2144,
			"JH": 2544,
			"KA": 6057,
			"KL": 6762,
			"LD": 0,
			"MP": 14529,
			"MH": 13370,
			"MN": 140,
			"ML": 131,
			"MZ": 95,
			"NL": 37,
			"OR": 6249,
			"PY": 127,
			"PB": 1969,
			"RJ": 11657,
			"SK": 62,
			"TN": 8648,
			"TR": 840,
			"UP": 14875,
			"UT": 786,
			"WB": 11887,
		},
		{
			"AP": 21484,
			"AR": 168,
			"AS": 6801,
			"BR": 6740,
			"CH": 224,
			"CT": 3757,
			"DN": 32,
			"DD": 9,
			"DL": 4544,
			"GA": 96,
			"GJ": 7279,
			"HR": 4617,
			"HP": 792,
			"JK": 2432,
			"JH": 2979,
			"KA": 6084,
			"KL": 7554,
			"LD": 1,
			"MP": 14321,
			"MH": 14452,
			"MN": 171,
			"ML": 176,
			"MZ": 125,
			"NL": 43,
			"OR": 6825,
			"PY": 149,
			"PB": 2242,
			"RJ": 12934,
			"SK": 47,
			"TN": 6489,
			"TR": 964,
			"UP": 16375,
			"UT": 1038,
			"WB": 12785,
		},
	]
	return json.dumps(data)
