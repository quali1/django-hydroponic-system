from django.urls import path
from . import views

urlpatterns = [
    path('', views.hydroponic_system_mixin_view, name="home"),
    path('<int:pk>/delete/', views.hydroponic_system_mixin_view),
    path('<int:pk>/update/', views.hydroponic_system_mixin_view),
    path('<int:pk>/', views.hydroponic_system_mixin_view),
]
