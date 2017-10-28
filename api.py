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
	return "dummy data"
