from email.mime import application
import re
from unittest import result
from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
board = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post",methods=['POST', 'GET'])
def post():
	value = request.form['input']
	msg = "%s 을 입력함." %value
	if request.method == 'POST':
		result = request.form
		return render_template("example.html", result = result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)