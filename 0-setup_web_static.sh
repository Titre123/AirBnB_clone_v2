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
test -e /data/web_static/releases/test/index.html || touch /data/web_static/releases/test/index.html
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
my_link="/data/web_static/current" 
if [ -L ${my_link} ] ; then
	if [ -e ${my_link} ] ; then
		rm -r /data/web_static/current
		ln -s /data/web_static/releases/test/ /data/web_static/current
	else
		ln -s /data/web_static/releases/test/ /data/web_static/current
	fi
else
	ln -s /data/web_static/releases/test/ /data/web_static/current
fi
chown ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a \tlocation /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
service nginx  restart
exit 0
