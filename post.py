from email.mime import application
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 을 입력함." %value #여기에 결과창 띄우기
	return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)