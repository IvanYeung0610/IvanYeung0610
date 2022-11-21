
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

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
    return render_template( 'main.html' )


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()