#Necessary flask import
from flask import Flask, render_template, redirect, url_for

#create F app
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    text= {'h1' : 'CD Assignment site' ,
           'p': 'To be able to deliver this app onto digital ocean we followed these steps', 
           'l' : {'Creating a droplet in Digital Ocean',
                  'Creating a new user, no sudo priviledges',
                  'Installing and setting up git in the server',
                  'Creating an empty repository',
                  'Creating a GitHub Actions .yml file for the deployment workflow',
                  'Creating and setting up a key-value pair between the server and GitHub',
                  'Properly storing your secrets',
                  'Writing into the .yml file the actions to deploy upon push',
                  'Installing the components to use pip',
                  'Creating a python virtual environment',
                  'Installing Flask, Gunicorn and Nginx',
                  'From your local machine, writing a sample Flask app and pushing the changes',
                  'In the server, creating /etc/systemd/system/myproject.service',
                  'Creating /etc/nginx/sites-available/myproject'
                  'Linking the myproject file from sites available to sites-enabled',
                  'Modifying the sudoers file to allow the updater user to run systemctl restart myproject.service as a part of the actions file'
                  'From the local machine, updating the flask app, adding a static folder and a css folder',
                  'Properly linking this within the flask app and pushing changes',
                  'From the server, modifying the myproject.service file to include a route to the static file',
                  'Creating requirements.txt in the repository folder',
                  'Setting up pytest and creating a test.py file to test the Flask app',
                  'Updating the .yml file to run pytest and only deploying if the tests are run succesfully',
                  'Within the server, creating a .sh file, including git pull and systemctl restart myproject.service',
                  'Replace the script portion in the .yml file with the single line "bash myprojectscript.sh"',
                  'Continue to update Flask app and test file from local machine and pushing changes'}
            }
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