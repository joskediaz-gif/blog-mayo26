from django.urls import path
from .views import BloglistView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns = [
    path('', BloglistView.as_view(), name='post-list'), 
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/crear/', BlogCreateView.as_view(), name='blog-create'),
    path('post/actualizar/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('post/eliminar/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
]
