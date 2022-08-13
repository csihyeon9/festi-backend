from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return'''
    <head>
	<meta charset="UTF-8">
	<title>HTML for python flask</title>
</head>

<body>
	<form action="/post" method="post">
	​	<p>이름 : <input type="text" id="input" name="input"></p>
		<p>이름을 입력하고 제출버튼을 누르세요. <input type="submit" value="제출" onclick="alert('제출 완료!')" /></p>
	</form>
</body>
    '''

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 을 입력함." %value #여기에 결과창 띄우기
	return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')