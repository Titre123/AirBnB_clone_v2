#!/usr/bin/env bash
# bash script that sets up your web servers for the deployment of web_static

if [[ ! `dpkg --get-selections | grep nginx` ]]; then
        apt -y update
        apt -y install nginx
        ufw allow 'Nginx HTTP'
fi
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
test -e /data/web_static/releases/test/index.html || sudo touch /data/web_static/releases/test/index.html
dir="/data/web_static/releases/test/index.html"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" > $dir
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
service nginx  restart
exit 0
