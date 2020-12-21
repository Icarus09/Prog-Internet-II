from django.db import models
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    
    class Meta:
        ordering =('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    profile = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.name