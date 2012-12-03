from django.conf.urls import patterns, url
from views import TweevieView

urlpatterns = patterns('',
	# Tweevie
	url(r'^tweevie/$', TweevieView.as_view(), name='tweevie'),
)
