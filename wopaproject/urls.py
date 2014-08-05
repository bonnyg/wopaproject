from django.conf.urls import patterns, include, url
from blog import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='index'),
	url(r'^blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
	url(r'^blog/category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),
	url(r'^post/new/$', views.post_new, name= "newpost"),

)
