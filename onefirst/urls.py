from django.conf.urls import url
from . import views

app_name = 'onefirst'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    # url(r'^search/$', views.search, name='search'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout', views.logout_view),
    url(r'^register$', views.register_view, name='register'),
]