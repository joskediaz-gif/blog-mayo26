from django.urls import path
from .views import BloglistView, BlogDetailView
urlpatterns = [
    path('', BloglistView.as_view(), name='blog-list'), 
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
