from fabric.api import local
from ohs_site import settings
import os

BUILD_DIR = settings.BUILD_DIR

def build_site():
    local("python manage.py build")

def build_static():
	pass

def build_blog():
	blog = settings.STATICBLOG_COMPILE_DIRECTORY
	if not os.path.exists(blog):
	    os.makedirs(blog)
	local("python manage.py update_blog")

def build():
	build_site()
	build_blog()
	build_static()