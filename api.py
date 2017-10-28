import json

from flask import Blueprint, request, abort

from models.dbmodels import session, FirearmTxn

view = Blueprint('api', __name__)


@view.route("/api/v1/get_arm_report", methods=["GET"])
def get_arm_report():
	data = request.args
	try:
		fromtime = data['fromtime']
		period = data['period']
		count = data['count']
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
