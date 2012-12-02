from fabric.api import local, abort, env

from fabric.contrib import django
django.project('ohs_site')
from django.conf import settings

import os

BUILD_DIR = settings.BUILD_DIR

def setup():
	local('cp ohs_site/offline/sample.env ohs_site/.env')
	local('nano ohs_site/.env')

def build_site():
	e = getattr(env, 'environment', None) 
	if e == 'production':
		local("foreman run python manage.py build --skip-media --skip-static")
	else:
		local("python manage.py build")
			

def build_extras():
	if not os.path.exists(BUILD_DIR):
		os.makedirs(BUILD_DIR)
	local('cp ohs_site/extras/* %s' % BUILD_DIR)


def build_blog():
	blog = settings.STATICBLOG_COMPILE_DIRECTORY
	if not os.path.exists(blog):
		os.makedirs(blog)

	e = getattr(env, 'environment', None) 
	if e == 'production':
		local("foreman run python manage.py update_blog")
	else:
		local("python manage.py update_blog")


def build():
	build_site()
	build_blog()
	build_extras()


def deploy():
	env.environment = 'production'
	build()
	local('foreman run python manage.py collectstatic --noinput')
	local('foreman run python manage.py assets build')
	local('ghp-import -p %s' % BUILD_DIR, capture=True)
	env.environment = None