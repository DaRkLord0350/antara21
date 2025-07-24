from django.urls import path
from . import views

app_name = 'portfolio'
# URL patterns for the portfolio app
urlpatterns = [
    path('', views.home, name='home'),
]