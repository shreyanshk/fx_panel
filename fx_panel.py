from flask import Flask, request, render_template
from models.dbmodels import session, FirearmTxn, Owner, Users, FirearmType


app = Flask(__name__)


@app.route("/", methods=["GET"])
def render_home():
	return render_template('homepage.j2')


@app.route("/control/arms/register", methods=["GET", "POST"])
def register_arm():
	if request.method == 'POST':
		pass
	else:
		return render_template('register_arm.j2')


@app.route("/api/v1/get_crime_report", methods=["GET"])
def get_crime_report():
	data = request.args
	return str(data)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
