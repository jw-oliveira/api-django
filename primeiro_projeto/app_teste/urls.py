from django.urls import path
from . import views

app_name = 'app_teste'

urlpatterns = [
    path("/index", views.index, name='index')
]