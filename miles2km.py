# Importing required functions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('mile_form.hmtl')

@app.route('/miletokm', methods=['POST'])
def miletokm():

    data = request.form
    value = int(data['mile'])
    value = value*1.609
    cm_str = "KM:  "+str(value)

    return cm_str

if __name__ == '__main__':
	# Run the application on the local development server
	app.run()
