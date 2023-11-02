# Importing required functions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('feet_form.html')

@app.route('/feettometers', methods=['POST'])
def feettometers():

    data = request.form
    value = int(data['feet'])
    value = value/3.281
    cm_str = "Meters:  "+str(value)

    return cm_str

if __name__ == '__main__':
	# Run the application on the local development server
	app.run()
