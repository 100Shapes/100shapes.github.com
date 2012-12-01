from bakery.views import BuildableTemplateView

class HomeView(BuildableTemplateView):

	template_name = "home.html"
	build_path = "index.html"
