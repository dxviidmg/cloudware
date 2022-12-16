from . import views
from django.urls import path

app_name = 'quotes'

urlpatterns = [
    path('cotiza', views.Cotiza.as_view(), name='cotiza'),
]