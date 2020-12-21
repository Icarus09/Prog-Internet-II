from django.shortcuts import render

import json
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .serializers import *

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ProfilePostList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-posts-list'

class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-posts-detail'

class PostCommentList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'

class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCommentSerializer
    name = 'post-comment-detail'

class CommentList(APIView):
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        comment_serializer = CommentSerializer(post.comments, many=True)
        return Response(comment_serializer.data)

    def post(self, request, pk, format=None):
        comment = request.data
        comment['postId'] = pk
        comment_serializer = CommentSerializer(data=comment)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
  
    def get_comment(self, post_pk, comment_pk):
        try:
            post = Post.objects.get(pk=post_pk)
            try:
                comment =  post.comments.get(pk=comment_pk)
                return comment
            except Comment.DoesNotExist:
                raise Http404
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_pk, comment_pk, format=None):
        comment = self.get_comment(post_pk,comment_pk)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)

    def put(self, request, post_pk, comment_pk, format=None):
        comment = self.get_comment(post_pk,comment_pk)
        comment_data = request.data
        comment_data['postId'] = post_pk
        comment_serializer = CommentSerializer(comment, data=comment_data)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, comment_pk, format=None):
        comment_serializer = CommentSerializer(data=request.data)
        comment = self.get_comment(post_pk,comment_pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)

class ProfilePostsCommentsList(APIView):
    def get(self, request, format=None):
        response = []
        profiles = Profile.objects.all()
        for profile in profiles:
            profile_data = {}
            
            profile_data['id'] = profile.id
            profile_data['name'] = profile.name

            count_posts = 0
            count_comments = 0

            for post in profile.posts.all():
                count_posts += 1
                for comment in post.comments.all():
                    count_comments += 1

            profile_data['total_posts'] = count_posts
            profile_data['total_comments'] = count_comments

            response.append(profile_data)

        return Response(response)
    name = 'profile-posts-comments'

class ApiRoot(APIView):
    name = 'api-root'

    if Profile.objects.count() == 0:
        
        data = json.load(open('db.json'))
        
        for user in data['users']:
            name = user['name']
            email = user['email']
            Profile.objects.create(name=name, email=email)

        for post in data['posts']:
            profile = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'], body=post['body'], profile=profile)

        for comment in data['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(id=comment['id'],
                                    name=comment['name'],
                                    email=comment['email'],
                                    body=comment['body'],
                                    post=post)

    def get(self, request, *args, **kwargs):
        url = 'http://localhost:8000/'
        return Response({
            'profiles': reverse(ProfileList.name, request=request),
            'profiles-detail': url + 'profile/<int:pk>',
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'post-comments': reverse(PostCommentList.name, request=request),
            'comment-list': url + 'posts/<int:pk>/comments',
            'comment-detail': url + 'posts/<int:post_pk>/comments/<int:comment_pk>',
            'profile-posts-comments': reverse(ProfilePostsCommentsList.name, request=request),
        })


  
