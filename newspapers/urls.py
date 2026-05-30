from django.urls import path
from .views import BloglistView, BlogDetailView, BlogCreateView, BlogUpdateView
urlpatterns = [
    path('', BloglistView.as_view(), name='post-list'), 
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/crear/', BlogCreateView.as_view(), name='blog-create'),
    path('post/actualizar/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
]
