from django.conf.urls import patterns, include, url

urlpatterns = patterns('staticblog.views',

    url(r'^$', 'archive', name="blog"),

    (r'^([\-\w]+)$', 'render_post'), # need to remove ending '/' to make the link work to posts
    (r'^git/receive', 'handle_hook'),
)