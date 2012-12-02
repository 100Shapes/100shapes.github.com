from django.conf.urls import patterns, include, url
from views import HomeView

urlpatterns = patterns('',
	# Home
	url(r'^$', HomeView.as_view(), name='home'),
)

