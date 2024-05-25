from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hydro.urls')),
    path('', include('users.urls')),
]
