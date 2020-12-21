from django.urls import path, include
from .views import *

urlpatterns = [
path('', ApiRoot.as_view(), name=ApiRoot.name),
path('profile/', ProfileList.as_view(), name=ProfileList.name),
path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),
path('profile-post/', ProfilePostList.as_view(), name=ProfilePostList.name),
path('profile-post/<int:pk>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),
path('post-comments/', PostCommentList.as_view(), name=PostCommentList.name),
path('post-comments/<int:pk>', PostCommentDetail.as_view(), name=PostCommentDetail.name),
path('posts/<int:pk>/comments/', CommentList.as_view()),
path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentDetail.as_view()),
path('profile-posts-comments/', ProfilePostsCommentsList.as_view(), name= ProfilePostsCommentsList.name),
]