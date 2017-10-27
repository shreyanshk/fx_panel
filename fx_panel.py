from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route("/control/arms/register", methods=["GET", "POST"])
def register_arm():
	if request.method == 'POST':
		pass
	else:
		return render_template('register_arm.j2')


@app.route("/", methods=["GET"])
def render_home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
