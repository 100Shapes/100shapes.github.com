from django_assets import Bundle, register

css = Bundle(
	'css/about.css',
	output='gen/about.css')

register('css_about', css)