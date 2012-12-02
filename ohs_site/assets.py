from django_assets import Bundle, register

js_base = Bundle(
	'js/vendor/jquery-1.8.2.min.js',
	'js/vendor/modernizr-2.6.1.min.js',
	output='gen/base.js')

register('js_base', js_base)