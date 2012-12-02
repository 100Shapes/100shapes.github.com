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

Run setup:

	fab setup

