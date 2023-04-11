#Necessary flask import
from flask import Flask, render_template, redirect, url_for
from cd_steps import step_list

#create F app
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    text= {'h1' : 'CD Assignment site' ,
           'p': 'To be able to deliver this app onto digital ocean we followed these steps', }
    steps = step_list()
    
    return render_template('base.html', title = 'Index', data = text, steps = steps )
    
@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/links")
def links():
    text= {'h1' : 'These are the tutorials I followed' , 'note': 'some information was not in the tutorials, if you struggle, click on the notest button to go to clarifications about the tutorial content and what I did differently, or to get information that i got from my teachers', 'p' : 'Useful links',
           '':[]}
    return render_template('base.html', title = 'Useful links', data = text )

@app.route("/sh")
def sh():
    text= {'h2': 'creating the script', 'p': 'to create an sh script'}
    return render_template('instructions.html', title = 'sh', data = text )