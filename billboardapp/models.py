from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone



class Posts(models.Model):
    user = models.ForeignKey(User)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    lastupdate_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    visible = models.BooleanField(default=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return 'title: %s, text: %s, author: %s' % (self.title, self.text, self.author)

class Comments(models.Model):
    post_id = models.ForeignKey(Posts, on_delete = models.CASCADE)
    author = models.CharField(max_length=200, default="no author")
    text_comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    visible = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text_comment





