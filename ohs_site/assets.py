from django_assets import Bundle, register

js_base = Bundle(
	'js/vendor/jquery-1.8.2.min.js',
	output='gen/base.%(version)s.js')

styles_base = Bundle(
	'css/reset.css',
	'css/base.css',
	output='gen/base.%(version)s.css')

styles_responsive = Bundle(
	'css/responsive.css',
	output='gen/responsive.%(version)s.css')

register('js_base', js_base)
register('css_base', styles_base)
register('css_responsive', styles_responsive)