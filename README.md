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

Done.


Generating the Site
-------------------

Make sure there's a `output/` in your project root that won't be added to the repo because of the .gitignore.

Then you can run:
	
	make html

Or, more usefully:

	make devserver

This will regenerate the entire site every time a file changes. You can find more info in the [Pelican Docs](http://docs.getpelican.com/en/3.0/getting_started.html#kickstart-a-blog).


Deploying
---------

Deploying's super easy:

	make github 
	 

I'm seeings Warnings
--------------------

	WARNING: Feeds generated without SITEURL

It's fine – when we publish, a `SITEURL` gets specified

	WARNING: Caught exception "'pelican.contents.Article object' has no attribute 'author_gravatar'"

It's to do with creating the avatar. We we build the new `author_gravatar` context variable using [pelican-gravatar-plus](https://bitbucket.org/redmonkey/pelican-plugin-gravatar-plus) we create that property, but because of the way Jinja template look it up, they `warn` first.

Notes
-----

### Unused Templates

Our theme (the `ohs-pelican-theme/` directory) contains a load of templates we've copied over from the stock 'simple' theme. We're not using most of them – ignore them for now.