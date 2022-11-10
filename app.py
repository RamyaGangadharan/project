from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def webpage1():
	try:
		return "Simple web application to display Hello World!"
	except Exception as e:
		return "Error in code"

if __name__ == "__main__":
	app.run()
