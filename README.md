100shapes Site
==============

This site is now build on Django.

It knows how to [render itself out to a static folder](https://github.com/datadesk/django-bakery) and also includes a [blog written in markdown files](https://github.com/cgrice/django-staticblog).

Getting set up
--------------

Make a virtual directory for the project:

	mkvirtualenv 100shapes.com

Clone the repo to where you normally keep code:

	cd ~/Projects/
	git clone git@github.com:100Shapes/100shapes.com.git 100shapes.com
	cd 100shapes.com/
	setvirtualenvproject

Install the requirements:

	pip install -r requirements.txt

Run setup and add your [S3 details](https://sites.google.com/a/onehundredshapes.com/info/credentials):

	fab setup

Link to the 100shapes posts:

	ln -s path/to/drive/Site/posts/ ohs_site/blog/

Building the Static site
------------------------

Run:

	fab build

and everything will be made in ohs_site/build/.

Deploying
---------

Make sure you've copied `.env` with your Amazon S3 details, run:

	fab deploy

