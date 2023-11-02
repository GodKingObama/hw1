# Importing required functions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('convert_form.html')

@app.route('/inch2cm', methods=['POST'])
def inch2cm():

    data = request.form
    value = int(data['inches'])
    value = value*2.54
    cm_str = "CM:  "+str(value)

    return cm_str

if __name__ == '__main__':
	# Run the application on the local development server
	app.run()

