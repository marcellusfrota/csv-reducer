from flask import Flask, flash, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__, template_folder='templates')
api = Api(app)
app.secret_key = 'super secret key'

@app.route("/")
@app.route("/home")
def index():
	flash('No selected file')
	return render_template('pages/home.html')

if __name__ == "__main__":
	# app.secret_key = 'super secret key'
	# app.secret_key = os.urandom(24)
	app.run()


# import random, threading, webbrowser

# port = 5000 + random.randint(0, 999)
# url = "http://127.0.0.1:{0}".format(port)

# threading.Timer(1.25, lambda: webbrowser.open(url) ).start()

# app.run(port=port, debug=False)