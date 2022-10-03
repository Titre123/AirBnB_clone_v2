!/usr/bin/python3
""" compress web_static files """

from fabric.operations import *
from datetime import datetime
import re
import os
date = datetime.now().strftime("%Y%m%d%H%M%S")


def do_pack():
    '''fab fucntion to compress web_static files'''
    local("mkdir -p versions")
    re = local("tar -cvzf versions/web_static_{}.tgz web_static"
               .format(date), capture=True)
    if re.failed:
        return None
    return re

def do_deploy(archive_path):
    ''' upload the web_static to web server '''
    env.hosts = ['3.238.125.126', '34.204.195.185']
    if os.path.exists(archive_path):
        res = put("{}".format(archive_path), "/tmp")
	    if res.failed:
		return False
	archive= "{}".format(archive_path)
        path= "/data/web_static/releases/{}/".format(re.split(r'[/.]',archive)[1])
	res = run("mkdir -p {}".format(path))
	    if res.failed:
		return False
	tmp_arch = "/tmp/{}".format(archive.split('/')[1])
	res = run("tar -xzf {} -C {}".format(tmp_arch, path)
	    if res.failed:
		return False
	res = run("rm {}".format(tmp_arch))
	    if res.failed:
		return False
	res = run("mv {}web_static/* {}".format(path,path))
	    if res.failed:
		return False
	res = run("rm -rf {}web_static".format(path))
	    if res.failed:
		return False
	res = run("rn -rf /data/web_static/current")
	    if res.failed:
		return False
	res = run("ln -s {} /data/web_static/current".format(path))
	    if res.failed:
		return False
	return True
    else:
        return False
