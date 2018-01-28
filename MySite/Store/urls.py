from django.urls import path
from . import views

# from django.contrib.auth.views import login

urlpatterns = [
    path(r'', views.home, name='home'),

]
