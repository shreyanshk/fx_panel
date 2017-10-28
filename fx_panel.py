from flask import Flask, request, render_template
from api import view as apiview


app = Flask(__name__)
app.register_blueprint(apiview)


@app.route("/", methods=["GET"])
def render_home():
	return render_template('homepage.j2')


@app.route("/control/arms/addtxn", methods=["GET", "POST"])
def register_arm():
	if request.method == 'POST':
		return "done"
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
