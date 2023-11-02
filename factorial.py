# Importing required functions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('factorial_form.html')

@app.route('/factorial', methods=['POST'])
def factorial():

    data = request.form
    value = int(data['X'])
    i = 1
    fac_value = 1
    while i <= value:
        fac_value =fac_value*i
        i += 1
    cm_str = "factorial("+str(value)+")="+str(fac_value)

    return cm_str

if __name__ == '__main__':
	# Run the application on the local development server
	app.run()
