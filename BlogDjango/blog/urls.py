from django.urls import path
from .views import home, BlogListView, BloggerListView, PostDetailView, add_comment, blogger_detail

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('bloggers/', BloggerListView.as_view(), name='blogger-list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/add_comment/', add_comment, name='add-comment'),
    path('blogger/<int:blogger_id>/', blogger_detail, name='blogger-detail'),
]
