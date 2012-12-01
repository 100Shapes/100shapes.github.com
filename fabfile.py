from fabric.api import local, abort

from fabric.contrib import django
django.project('ohs_site')
from django.conf import settings

import os

BUILD_DIR = settings.BUILD_DIR

def setup():
	local('cp ohs_site/offline/local_settings.py ohs_site/', capture=False)

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

def deploy():
	build()
	abort("Deploying isn't set up yet. Fix me.")