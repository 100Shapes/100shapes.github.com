from fabric.api import local, abort

from fabric.contrib import django
django.project('ohs_site')
from django.conf import settings

import os, shutil

BUILD_DIR = settings.BUILD_DIR
BUILT_STATIC_DIR = os.path.join(BUILD_DIR, 'static')

def setup():
	local('cp ohs_site/offline/secret_settings.py ohs_site/')
	local('nano ohs_site/secret_settings.py')

def build_site():
    local("python manage.py build")

def build_static():
	print "Not implemented"

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
	os.environ['PRODUCTION'] = '1'
	build()
	shutil.rmtree(BUILT_STATIC_DIR)
	local('ghp-import %s' % BUILD_DIR)
	del os.environ['PRODUCTION']
	abort("Deploying isn't set up yet. Fix me.")