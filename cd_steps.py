def step_list():
   steps = [
                ('User',['Creating a droplet in Digital Ocean',
                  'Creating a new user, no sudo priviledges',
                  'Installing and setting up git in the server',
                  'Creating a new git user with the same email as your GitHub']), 
                ('Deployment',['Creating an empty repository',
                  'Creating a GitHub Actions .yml file for the deployment workflow',
                  'Creating and setting up a key-value pair between the server and GitHub',
                  'Properly storing your secrets',
                  'Writing into the .yml file the actions to deploy upon push',
                  ]),
                ('Nginx/gunicorn',['Installing the components to use pip',
                  'Creating a python virtual environment',
                  'Installing Flask, Gunicorn and Nginx',
                  'From your local machine, writing a sample Flask app and pushing the changes',
                  'In the server, creating /etc/systemd/system/myproject.service',
                  'Creating /etc/nginx/sites-available/myproject',
                  'Linking the myproject file from sites-available to sites-enabled',
                  'Modifying the sudoers file to allow the updater user to run systemctl restart myproject.service as a part of the actions file',
                  'From the local machine, updating the flask app, adding a static folder and a css folder',
                  'Properly linking this within the flask app and pushing changes',
                  'From the server, modifying the myproject.service file to include a route to the static file']),
                ('Pytest',['Creating requirements.txt in the repository folder',
                  'Setting up pytest and creating a test.py file to test the Flask app',
                  'Updating the .yml file to run pytest and only deploying if the tests are run succesfully']),
                ('.sh',[ 'Within the server, creating a .sh file, including git    pull and systemctl restart myproject.service',
                  'Replace the script portion in the .yml file with the single line "bash myprojectscript.sh"',
                  'Continue to update Flask app and test file from local machine and pushing changes'])
            ]
   return steps

def useful_links(type):
   links_user = [('title','User'),('How to create a droplet', 'https://docs.digitalocean.com/products/droplets/how-to/create/'),('How to create a new ubuntu user','https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-ubuntu-20-04'),('How to set up and create new git user','https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04')]
   links_deployment = [('title','Deployment'),('Connecting GitHub with your server','https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2'),('note', 'This tutorial uses the root user, this is not recommended, my recommendation is to change into a user created solely for this purpose with no sudo priviledges.'), ('note', 'To grant systemctl restart permissions to the updater user, go to your /etc/sudoers file and add "updateruser ALL=NOPASSWD: /bin/systemctl restart myproject.service", or the same with "/usr/bin/systemctl", you can find out wich is necesary by running "which systemctl"'),('note', 'Remember to run the ssh key creation with this user, and to add your email to the command as such “ssh-keygen -t rsa -C "your_email@youremail.com"”')]
   links_nginx = [('title','Nginx/Gunicorn'),('Setting up NginX and Gunnicorn for your flask app','https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04'),('note','In the configuration files in "/etc/nginx/sites-available/myproject", make sure to add "location /CD/static {root /home/gitupdater/CD;}" so your static files get loaded as well'), ('Flask Templates', 'https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application')]
   links_pytest = [('title','pytest'),('Creating requirements.txt','https://www.scaler.com/topics/how-to-create-requirements-txt-python/'),('Setting up Pytest in GitHub actions','https://vilisimo.com/blog/setting-up-pytest-with-github-actions/'), ('Testing a flask app','https://flask.palletsprojects.com/en/2.2.x/testing/')]
   links_sh = [('title','.sh script'),('Making an sh script','https://www.guru99.com/introduction-to-shell-scripting.html'),('note','Replace the script portion in the .yml file with the single line "bash myprojectscript.sh"')]

   if type == 'user':
      return links_user
   
   elif type == 'deployment':
      return links_deployment
   
   elif type == 'nginx':
      return links_nginx
   
   elif type == 'pytest':
      return links_pytest
   
   elif type == 'sh':
      return links_sh
   
   else:

      links = [links_user, links_deployment, links_nginx, links_pytest, links_sh]
      return links
   