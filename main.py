#Necessary flask import
from flask import Flask

#create F app
app = Flask(__name__)

#Assign function to be called upon the '/' path request
@app.route("/")
def index():
    return 'Hello, world! This is the CD site'

@app.route("/cow")
def cow():
    return 'MOoooOo!'