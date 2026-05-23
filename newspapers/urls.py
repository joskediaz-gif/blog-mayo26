from django.urls import path
from .views import BloglistView
urlpatterns = [
    path('', BloglistView.as_view(), name='blog-list'), 
]