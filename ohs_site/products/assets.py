from django_assets import Bundle, register

styles_tweevie = Bundle(
	'css/tweevie.css',
	output='gen/tweevie.css')

register('css_tweevie', styles_tweevie)