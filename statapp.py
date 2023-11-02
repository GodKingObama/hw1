# Importing required functions
from flask import Flask, request, render_template
import fileinput
import sys
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('statapp_form.html')

@app.route('/stat', methods=['POST'])
def stat():

    data = request.form
    input_line = data['scores']
    scores=input_line.split(",")

    for i in range(len(scores)):
        scores[i]=int(scores[i])

    mean = sum(scores) / len(scores)
    res = sum((x - mean) ** 2 for x in scores) / len(scores)
    sd = math.sqrt(res)

    scores.sort()
    length = len(scores)
    i = (int)(length/2)
    if length%2 == 0:
        median = (scores[i-1]+scores[i])/2
    else:
        median = scores[i]

# printing result
    ret = "<html>The mean of list is : " + str(mean)+ "</br>"
    ret += "The variance of list is : " + str(res) + "</br>"
    ret += "The sd of list is : " + str(sd) +"</br>" 
    ret += "The median of list is:"+str(median)+"<html>"

    return ret

if __name__ == '__main__':
	# Run the application on the local development server
	app.run()
