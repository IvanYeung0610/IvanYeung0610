'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K02 -- flask-forms
2022-10-14
time spent: 1.5 hr
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not.
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #returns <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) #returns the URL of the page(<Request 'http://127.0.0.1:5000/' [GET]>)
    print("***DIAG: request.args ***")
    print(request.args) #returns ImmutableMultiDict([]) along with its contents if present
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers) #returns information on the machine and the web browser accessing the link
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #returns <Flask 'app'>
    print("***DIAG: request obj ***")
    print(request) #returns the URL of the page(<Request 'http://127.0.0.1:5000/auth?username=hi&sub1=Submit+Query' [GET]>)
    print("***DIAG: request.args ***")
    print(request.args) #returns ImmutableMultiDict([]) along with its contents if present (ex. ImmutableMultiDict([('username', 'hi'), ('sub1', 'Submit Query')]))
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) #returns the string that was inputted into the query and submitted
    print("***DIAG: request.headers ***")
    print(request.headers) #returns information on the machine and the web browser accessing the link
    #return f"{request.args['username']} is AWESOME" #replaces the variable in the f string with the inputted value.
    return "Waaaa hooo HAAAH"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
