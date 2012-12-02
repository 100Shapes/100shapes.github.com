from django.conf.urls import patterns, url
from views import MooView

urlpatterns = patterns('',
	# Moo
	url(r'^moo/$', MooView.as_view(), name='moo'),
)
