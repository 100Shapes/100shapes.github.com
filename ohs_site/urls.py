from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', include('ohs_site.home.urls')),
	url(r'^blog/', include('ohs_site.blog.urls')),
	url(r'^case-studies/', include('ohs_site.case_studies.urls')),

)
