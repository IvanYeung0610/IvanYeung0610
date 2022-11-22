'''
Ivan Yeung and Vivian Graeber
SoftDev
K20 -- REST API
2022-11-21
time spent:  .8
'''
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import requests #https request module
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

file = open("key_nasa.txt", "r")
NASA_API_KEY = file.readline()
print("NASA_API_KEY: " + NASA_API_KEY)

API_URL = "https://api.nasa.gov/planetary/apod?api_key=" + NASA_API_KEY
print(API_URL)

r = requests.get(API_URL) #creating a response object that will get us the information we need
print("********************Server Response Body********************")
print(r.content) # shows the content of what the request got from the URL



@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'main.html' )


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
