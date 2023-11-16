from django.urls import path
from . import views
from .views import BookCreateView

app_name = 'app_teste'

urlpatterns = [
    path("/index", views.index, name='index'),
    path("/books", BookCreateView.as_view(), name='book-create'),
]