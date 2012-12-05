from django_assets import Bundle, register

css = Bundle(
	'css/blog.css',
	output='gen/blog.css')

register('css_blog', css)