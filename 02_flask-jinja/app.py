'''
ZIMZIM(mermann Telegram) Ziying Jian, Maya Nelson, Ivan Yeung
SoftDev
K02 -- flask-jinja
2022-10-13
time spent: 0 hr
'''

'''
PREDICTIONS:
Q0. We think that we won't be able to access the webpage because the render_template seems to be part of the route.
Q1. We think that the URL that the page will use to load will be the same as the other app.py files that we have run: http://127.0.0.1:5000
Q2. We think the first argument will be the html file that will be shown when we use the URL from flask when running the program.
The second parameter might be part of the address of the URL like the files that we requested in the static folder from 09.
The final parameter is a variable used to replace the variable holders({}) in the f string structures inside the html file.

DISCOS:
- Both fire fox and Vivaldi return a page with:
{% for item in collection %} {{ item }}
{% endfor %}
when opening the html file from the file directory.


QCC:
- What does the 

'''

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

if __name__ == "__main__":
    app.debug = True
    app.run()
