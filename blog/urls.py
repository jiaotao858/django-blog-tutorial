from django.contrib import admin
from django.conf.urls import include, url
from onefirst.feeds import AllPostsRssFees

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', include('onefirst.urls')),
    url(r'', include('comments.urls')),
    url(r'all/rss/$', AllPostsRssFees(), name='rss'),
    url(r'search/', include('haystack.urls')),
]
