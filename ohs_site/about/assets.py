from django_assets import Bundle, register

css = Bundle(
	'css/about.css',
	output='gen/about.%(version)s.css')

register('css_about', css)