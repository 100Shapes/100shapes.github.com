from bakery.views import BuildableTemplateView
from django.core.urlresolvers import reverse

class MooView(BuildableTemplateView):

	template_name = "moo.html"
	build_path = '/case-studies/moo/index.html'#'/'.join(reverse('moo'), "index.html",)
