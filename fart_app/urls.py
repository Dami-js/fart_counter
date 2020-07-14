from django.urls import path
from fart_app import views

urlpatterns = [
    path('', views.home, name = 'home' )
]
