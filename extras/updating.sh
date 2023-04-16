#! /bin/sh
cd ~/CD/
git pull
sudo systemctl restart cd-site.service
echo 'Deployment commands run'
