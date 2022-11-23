'''
Ivan Yeung
SoftDev
K20 -- REST API
2022-11-21
time spent:  0.0hr
'''
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import urllib.request
import requests #https request module
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

country = "brazil"

API_URL = f"https://restcountries.com/v3.1/name/{country}"
print("***DIAG: API url ***")
print(API_URL)

r = requests.get(API_URL) #creating a response object that will get us the information we needr
api_dict = r.json() #r.json() returns a dictonary after deconding the response object
population = (api_dict[0])["population"]
print("Population of Brazil: " + str(population))


@app.route("/" , methods=['GET', 'POST'])
def disp_loginpage():
    return 


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()