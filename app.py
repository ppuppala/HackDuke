from flask import Flask, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
	return send_from_directory('./', 'coartindex.html')

@app.route('/inspireme.html')
def index2():
	return send_from_directory('./', 'inspireme.html')

@app.route('/iminspired.html')
def index3():
	return send_from_directory('./', 'iminspired.html')



app.run(debug=True)