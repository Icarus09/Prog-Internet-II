from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('name', 'email')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'post')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='name')

    class Meta:
        model = Post
        fields = ('title', 'body', 'profile')

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'email', 'posts')


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'profile', 'comments')

