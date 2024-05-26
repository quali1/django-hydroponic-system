from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('systems/', views.hydro_list_view, name='systems-list')
]
