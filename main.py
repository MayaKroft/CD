#Necessary flask import
from flask import Flask, render_template, redirect, url_for

#create F app
app = Flask(__name__)

#Assign function to be called upon the '/' path request
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
