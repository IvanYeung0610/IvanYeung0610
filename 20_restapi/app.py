
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'main.html' )


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
