from fabric.api import local, abort

from fabric.contrib import django
django.project('ohs_site')
from django.conf import settings

import os

BUILD_DIR = settings.BUILD_DIR

def setup():
	local('cp ohs_site/offline/secret_settings.py ohs_site/')
	local('nano ohs_site/secret_settings.py')

def build_site(include_assets=True):
	if include_assets:
	 	local("python manage.py build")
	else:
		local("python manage.py build --skip-media --skip-static")
	
		
def build_extras():
	if not os.path.exists(BUILD_DIR):
		os.makedirs(BUILD_DIR)
	local('cp ohs_site/extras/* %s' % BUILD_DIR)

def build_blog():
	blog = settings.STATICBLOG_COMPILE_DIRECTORY
	if not os.path.exists(blog):
		os.makedirs(blog)
	local("python manage.py update_blog")

def build(include_assets=True):
	build_site(include_assets)
	build_blog()
	build_extras()

def deploy():
	os.environ['PRODUCTION'] = '1'
	build(False)
	local('ghp-import -p %s' % BUILD_DIR, capture=True)
	del os.environ['PRODUCTION']
	