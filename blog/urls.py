from django.urls import path
from .views import BlogView, ArticleDetailView, AddPostView
from . import views

urlpatterns = [
	path('blog/', BlogView.as_view(), name="blog"),
	path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
	path('add_post/', AddPostView.as_view(), name='add_post'),
]