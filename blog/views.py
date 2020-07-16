from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm



class BlogView(ListView):
	model = Post
	#paginate_by = 2
	template_name = 'blog.html'
	ordering = ['-post_date']
	



class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'




class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

'''class AddCommentView(CreateComment):
	model = Post
	form_class = CommentForm
	template_name = 'add_comment.html'''
	

