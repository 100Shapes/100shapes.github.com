from django.conf.urls import patterns, include, url
from home.views import HomeView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    # Home
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^blog/', include('ohs_site.blog.urls'))

    # url(r'^ohs_site/', include('ohs_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
