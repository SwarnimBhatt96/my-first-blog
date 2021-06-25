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
    
    
    def __str__(self):
        return self.title