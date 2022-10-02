#!/usr/bin/env bash
# bash script that sets up your web servers for the deployment of web_static

if [[ ! `dpkg --get-selections | grep nginx` ]]; then
        sudo apt -y update
        sudo apt -y install nginx
fi
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
test -e /data/web_static/releases/test/index.html || sudo touch /data/web_static/releases/test/index.html
dir="/data/web_static/releases/test/index.html"
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" > $dir
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx  restart
exit 0
