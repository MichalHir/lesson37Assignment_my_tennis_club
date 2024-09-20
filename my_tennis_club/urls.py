
from django.contrib import admin
from django.urls import include, path

from courts import views

urlpatterns = [
    path('courts/', include('courts.urls')),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]
