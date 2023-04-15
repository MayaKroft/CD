#Necessary flask import
from flask import Flask, render_template, redirect, url_for
from cd_steps import step_list, useful_links

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
    text= {'h2' : 'These are the tutorials I followed' , 'p': 'Some information was not in the tutorials, thus there are some notes amongst the links here'}
    return render_template('instructions.html', title = 'Useful links', data = text, links = useful_links("all") )
