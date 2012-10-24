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


Getting the Posts
-----------------

Symlink `posts/` and `pages/` from our Google Drive:

	ln -s path/to/drive/Company\ Wide/Site/posts/ 
	ln -s path/to/drive/Company\ Wide/Site/pages/ 
	 