100shapes.com
=============

100shapes built using [Pelican](http://docs.getpelican.com/en/3.0/).

Getting set up
--------------

Make a virtual directory for the project:

	mkvirtualenv 100shapes.com

Clone the repo to where you normally keep code:

	cd ~/Projects/
	git clone git@github.com:100Shapes/100shapes.com.git

Set the project root:

	cd 100shapes.com/
	setvirtualenvproject

Install the requirements:

	pip install -r requirements.txt

Done.


Generating the Site
-------------------

Make sure there's a `output/` in your project root that won't be added to the repo because of the .gitignore.

Then you can run:
	
	make html

Or, more usefully:

	make devserver

This will regenerate the entire site every time a file changes. You can find more info in the [Pelican Docs](http://docs.getpelican.com/en/3.0/getting_started.html#kickstart-a-blog).


Getting the Posts
-----------------

Symlink `posts/` and `pages/` from our Google Drive:

	ln -s path/to/drive/Company\ Wide/Site/posts/ content
	ln -s path/to/drive/Company\ Wide/Site/pages/



Stuff to still do
----------------- 
	 
### Blog Homepage

Posts get built into `blog/`, but we need an index page in there with a list of posts. Maybe this has to be a `page`. See [Pelican Docs](http://docs.getpelican.com/en/3.0/).