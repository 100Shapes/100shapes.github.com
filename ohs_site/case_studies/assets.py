from django_assets import Bundle, register

styles_moo = Bundle(
	'css/moo.css',
	output='gen/moo.%(version)s.css')

register('css_moo', styles_moo)