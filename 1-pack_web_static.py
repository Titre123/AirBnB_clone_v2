#!/usr/bin/python3
# compress web_static files
from fabric.operations import *
from datetime import datetime
date = datetime.now().strftime("%y%m%d%H%M%S")
def do_pack():
	'''fab fucntion to compress web_static files'''
	local('mkdir -p versions')
	file = f"versions/web_static_{date}.tgz"
	re = local(f'tar -cvzf {file} ~/AirBnB_clone_v2/web_static', capture=True)
	
	if re.failed:
		return None
	return re
