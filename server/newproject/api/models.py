from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
 
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username
class Books(models.Model):
    book_name = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    book_author = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

   
    favorited_by = models.ManyToManyField(CustomUser, through='UserBooks', related_name='favorite_books')

    def __str__(self):
        return self.book_name

class UserBooks(models.Model):
  
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    
 
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')