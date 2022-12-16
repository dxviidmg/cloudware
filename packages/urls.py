from . import views
from django.urls import path

app_name = 'packages'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about-us', views.AboutUs.as_view(), name='about-us'),
    path('packages', views.Packages.as_view(), name='packages-list')
]