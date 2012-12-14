from django_assets import Bundle, register

js = Bundle(
	'js/vendor/jquery.scrollto.js',
	'js/home.js',
	output='gen/home.%(version)s.js')

css = Bundle(
	'css/home.css',
	output='gen/home.%(version)s.css')

register('js_home', js)
register('css_home', css)