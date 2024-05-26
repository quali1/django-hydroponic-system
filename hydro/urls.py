from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('systems/', views.HydroListView.as_view(), name='systems-list'),
    path('measurements/', views.MeasurementsListView.as_view(), name='measurements-list'),
]
