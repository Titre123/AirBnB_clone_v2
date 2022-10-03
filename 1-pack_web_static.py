#!/usr/bin/python3
# compress web_static files
from fabric.operations import *
from datetime import datetime
date = datetime.now().strftime("%Y%m%d%H%M%S")
def do_pack():
	'''fab fucntion to compress web_static files'''
	local('mkdir -p versions')
	re = local('tar -cvzf versions/web_static_{} ~/AirBnB_clone_v2/web_static'
		   .format(date), capture=True)
	
	if re.failed:
		return None
	return re
