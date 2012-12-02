from bakery.views import BuildableTemplateView
from django.core.urlresolvers import reverse

class MooView(BuildableTemplateView):

	template_name = "moo.html"
	
	@property
	def build_path(cls):
		return '/'.join((reverse('moo')[1:], "index.html",))
