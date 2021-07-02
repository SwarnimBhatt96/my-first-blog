
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    
    # class/model variables
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishDate = models.DateTimeField(null=True, blank=True)
    
    
    # class/model functions 
    
    def publish(self):
        self.publishDate = timezone.now()
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approvedComment=True)
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blogApp.Post', on_delete=models.CASCADE, related_name='comments')
    # he related_name option in models.ForeignKey allows us to have access to comments from within the Post model.
    author = models.CharField(max_length=255)
    text = models.TextField()
    createddate = models.DateTimeField(default = timezone.now)
    approvedComment = models.BooleanField(default = False)
    
    def approve(self):
        self.approvedComment = True
        self.save()
        
    def __str__(self):
        return self.text