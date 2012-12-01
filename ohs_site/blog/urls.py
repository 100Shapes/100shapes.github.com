from django.conf.urls import patterns, include, url


urlpatterns = patterns('staticblog.views',

    url(r'^$', 'archive', name="blog"),

    (r'^([\-\w]+)$', 'render_post'),
    (r'^git/receive', 'handle_hook'),
)