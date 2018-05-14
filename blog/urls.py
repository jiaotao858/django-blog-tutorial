from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'onefirst/', include('onefirst.urls')),
    url(r'', include('comments.urls')),
    url(r'admin/', admin.site.urls),
]
