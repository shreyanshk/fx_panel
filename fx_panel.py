from datetime import datetime

from flask import Flask, request, render_template, abort
from api import view as apiview
from models.dbmodels import Owner, session, FirearmTxn

app = Flask(__name__)
app.register_blueprint(apiview)


@app.route("/", methods=["GET"])
def render_home():
	return render_template('homepage.j2')


@app.route("/control/arms/addtxn", methods=["GET", "POST"])
def register_arm():
	if request.method == 'POST':
		try:
			userTypeRadio = request.args['userTypeRadio']
			ownerAdhaar = request.args['ownerAdhaar']
			date = request.args['date']
			serialNo = request.args['serialNo']
			inputType = request.args['inputType']
			previousAdhaar = request.args['previousAdhaar']
			if userTypeRadio is "New":
				name = request.args['name']
				number = request.args['number']
				address = request.args['address']
				city = request.args['city']
				state = request.args['state']
				data = {
					'name': name,
					'mobile': number,
					'address': address,
					'city': city,
					'state': state,
					'aadhar': ownerAdhaar
				}
				newownerentry = Owner(**data)
				session.add(newownerentry)
				data = {
					'txtype': inputType,
					'serialNo': serialNo,
					'origowner': previousAdhaar,
					'newowner': newownerentry.aadhar,
					'date': date,
				}
				firearmtx = FirearmTxn(**data)
				session.add(firearmtx)
				session.commit()
				return "", 200
			elif userTypeRadio is "Registered":
				olduser = session.query(Owner).filter(
					Owner.aadhar == previousAdhaar,
				).one()
				data = {
					'txtype': inputType,
					'serialNo': serialNo,
					'origowner': olduser.id,
					'newowner': ownerAdhaar,
					'date': date,
				}
				firearmtx = FirearmTxn(**data)
				session.add(firearmtx)
				session.commit()
			else:
				return "", 404
		except KeyError:
			return "", 404
	else:
		return render_template('register_arm.j2')


@app.route("/control/arms/findarm", methods=["GET"])
def find_arm():
	return render_template("find-arm.j2")


@app.after_request
def add_header(response):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	response.headers['Cache-Control'] = 'no-cache'
	return response


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
