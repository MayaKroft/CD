#Necessary flask import
from flask import Flask, render_template, redirect, url_for

#create F app
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    text= {'h1' : 'Hello, world! This is the CD site!' , 'p' : 'This is rendered through a template'}
    return render_template('base.html', title = 'Index', data = text )
    
@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/cow")
def cow():
    text= {'h1' : 'MOoooOo' , 'p' : 'MooOOoo'}
    return render_template('base.html', title = 'Moo', data = text )

@app.route("/sh")
def sh():
    text= {'h2': 'creating the script', 'p': 'to create an sh script'}
    return render_template('instructions.html', title = 'sh', data = text )