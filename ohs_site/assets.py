from django_assets import Bundle, register

js_base = Bundle(
	'js/vendor/jquery-1.8.2.min.js',
	output='gen/base.%(version)s.js')

styles_base = Bundle(
	'css/reset.css',
	'css/base.css',
	'css/responsive.css',
	output='gen/base.%(version)s.css')

register('js_base', js_base)
register('css_base', styles_base)
