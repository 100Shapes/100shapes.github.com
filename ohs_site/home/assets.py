from django_assets import Bundle, register

js = Bundle(
	'js/vendor/jquery.scrollto.js',
	'js/home.js',
	output='gen/home.js')

register('js_home', js)