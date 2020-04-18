from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    categorize=models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.categorize



class Article(models.Model):    
    title = models.CharField(max_length=100)    
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
       ordering = ['-date']

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] + '...'



class Comment(models.Model):
    content=models.CharField(max_length=500, verbose_name ="Add a Comment")
    post=models.ForeignKey(Article,related_name="comments",on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content