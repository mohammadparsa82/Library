from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

class Post(models.Model):
    tag = TaggableManager()
    author = models.CharField(max_length= 150)
    name_book = models.CharField(max_length= 250)
    content = models.TextField()
    status = models.BooleanField()
    counted_view = models.IntegerField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    login_require = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "{} - {}".format(self.id, self.name_book)
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})

class comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default= False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name



