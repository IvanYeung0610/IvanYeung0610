'''
Ivan Yeung and Vivian Graeber
SoftDev
K20 -- REST API
2022-11-21
time spent:  1.0
'''
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import urllib.request
import requests #https request module
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

with open("key_nasa.txt", "r") as file: #Using with statement automatically closes file after use
    NASA_API_KEY = file.read()

print("***DIAG: API key read in from key_nasa.txt ***")
print("NASA_API_KEY: " + NASA_API_KEY)

API_URL = "https://api.nasa.gov/planetary/apod?api_key=" + NASA_API_KEY
print("***DIAG: API key appended to https ***")
print(API_URL)

r = requests.get(API_URL) #creating a response object that will get us the information we need
# print("***DIAG: the contents of .content command ***")
# print(r.content) # shows the content of what the request got from the URL
# print("***DIAG: the contents of .json command ***")
# print(r.json()) #json decoder
api_dict = r.json() #r.json() returns a dictonary after deconding the response object
image_link = api_dict['hdurl'] #gets image from dictionary
explanation = api_dict['explanation'] #gets explaination from dictionary
title = api_dict['title']


@app.route("/" , methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'main.html', image=image_link, explanation=explanation alt_text=title)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
