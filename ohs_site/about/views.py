from bakery.views import BuildableTemplateView
from django.core.urlresolvers import reverse


class AboutView(BuildableTemplateView):

	template_name = "about.html"
	
	@property
	def build_path(cls):
		return '/'.join((reverse('about')[1:], "about.html",))