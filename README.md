100shapes.com
=============

100shapes.com built using [Pelican](http://docs.getpelican.com/en/3.0/).

Don't know what work to do? Look at the [100Shapes project backlog](https://www.pivotaltracker.com/projects/671939#).

Getting set up
--------------

Make a virtual directory for the project:

	mkvirtualenv 100shapes.com

Clone the repo to where you normally keep code:

	cd ~/Projects/
	git clone git@github.com:100Shapes/100shapes.github.com.git

Set the project root:

	cd 100shapes.github.com/
	setvirtualenvproject

Make the output dir:

	mkdir output

Install the requirements:

	pip install -r requirements.txt

Symlink `posts/` and `pages/` from our Google Drive:

	ln -s path/to/drive/Company\ Wide/Site/ content

Now copy `sample.env` to `.env`. This file won't be added to the repo:

	cp sample.env .env

Open you `.env` file and fill in the vars with our [Amazon S3 details](https://sites.google.com/a/onehundredshapes.com/info/credentials).

Make sure you've got `foreman` installed:

	which foreman


Running the Site
----------------

Make sure there's a `output/` in your project root that won't be added to the repo because of the .gitignore.

Then you can run:
	
	foreman start

This will regenerate the entire site every time a file changes. You can find more info in the [Pelican Docs](http://docs.getpelican.com/en/3.0/getting_started.html#kickstart-a-blog).


Deploying
---------

Deploying's super easy:

	make github 
	 

I'm seeings Warnings
--------------------

	WARNING: Feeds generated without SITEURL

It's fine – when we publish, a `SITEURL` gets specified


Notes
-----

### Unused Templates

Our theme (the `ohs-pelican-theme/` directory) contains a load of templates we've copied over from the stock 'simple' theme. We're not using most of them – ignore them for now.