from django.conf.urls import patterns, include, url
from views import AboutView

urlpatterns = patterns('',
	# About
	url(r'^$', AboutView.as_view(), name='about'),
)

