# CD asignment by X M K M 

For this assignment the following was performed:

The creation of a new user with limited permissions:
   The first tutorial found, only focused on using root as the user, which is not a good idea to establish a continuous deployment pipeline with git, acordig to the github documentation, git commands do not need to be executed with sudo priviledges.
   The user was created as usual with adduser.
   No sudo permissions were granted.
   The sudoers file was modified to ensure the user was able to restart the server after an update and only use the powerfull systemctl commant for this purpose.
   

SSH pairing with github and the server:
   An ssh key-pair was generated, after several unsuccesfull tries where the retrievalof the repository data would work from the command line in DigitalOcean but not the GitHub Actions script, I realized getting it to work required a git setup, including a git user to be created and for this user to have an email included in the GitHub account the git repository was going to connect to and that a new key needed to be generated. 
   The approppriate secrets were created and stored.
Setting up the GitHub Action file:
   The deployment job was setup to run only if the pytest job had been compelted successfully.
   The challenge lied in getting the correct requirement list so the pytest would work, several modules were required because the testing ran on a flask application. Realizing wich modules to leave in the requirements.txt file was mostly performed by trial and error, removing the modules that GitHub Actions mentioned as problematic.

The setup through the root user by modifying the nginx and gunicorn configuraiton files:
   The setting files were modified through the root user, as the updater does not have permissions within these directories, to serve the new page wich would be hosted in a folder that belongs to the updating user, the challenge lied in getting the static files served, after some research and several failed attempts, the appropriate syntax was found.

The creation of a .sh script to be run through actions:
   This sh script does not form part of the public git repository, but it goes get run as part of the script that the deployment action runs.


Additionally, per suggestion of some articles from Digital Ocean, the app is now served making use of it's own virtual environment.


