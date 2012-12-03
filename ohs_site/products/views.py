from bakery.views import BuildableTemplateView
from django.core.urlresolvers import reverse

class TweevieView(BuildableTemplateView):

	template_name = "tweevie.html"
	
	@property
	def build_path(cls):
		return '/'.join((reverse('tweevie')[1:], "index.html",))
