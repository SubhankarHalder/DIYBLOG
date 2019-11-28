from django.db import models
from datetime import date
from django.urls import reverse #Generate URLS by reversing URL patterns
from django.contrib.auth.models import User #Imports User for Author and/or Commentor

# Create your models here.
class Blog(models.Model):
    """ Model representing a Blog Post """
    name = models.CharField('Blog Post Title', max_length = 200, help_text = "Enter the title of the Blog Post")
    description = models.TextField('Blog Post', max_length = 1000, help_text = "Type your blog here")
    author = models.ForeignKey('BlogAuthor', on_delete = models.SET_NULL, null = True)
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        """ Returns the URL to access a particular blog instance """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """ String to represent the Model Object """
        return self.name

class BlogAuthor(models.Model):
    """Model representing Model Author"""
    name = models.OneToOneField(User, on_delete = models.SET_NULL, null = True)
    bio = models.TextField("Author Biography", max_length = 1000, help_text = "Enter a brief bio")

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        """ Returns the URL to access a particular blog author instance """
        return reverse('blog-author-detail', args=[str(self.id)])

    def __str__(self):
        """ String to represent the Model Object """
        return self.name.username

class BlogComment(models.Model):
    """Model representing Blog Comment"""
    description = models.TextField("Comment", max_length = 1000, help_text = "Enter Comment")
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    post_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["post_date"]

    def __str__ (self):
        """ String for representing Model Object """
        length = 40
        if len(self.description)>length:
            brief_comment = self.description[:length] + "..."
        else:
            brief_comment = self.description

        return self.description
