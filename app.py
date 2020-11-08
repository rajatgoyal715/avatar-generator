from flask import Flask, render_template, request
import generator
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def hello():
	avatar_file_name = 'static/avatar.png'
	avatar_file_path = os.path.abspath(avatar_file_name)

	generator.main(['-f', avatar_file_path])
	return render_template('index.html')
