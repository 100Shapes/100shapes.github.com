from django_assets import Bundle, register

css = Bundle(
	'css/blog.css',
	output='gen/blog.%(version)s.css')

register('css_blog', css)