from django.db import models

class Users(models.Model):
    user_mail = models.EmailField(max_length=150, unique=True)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user_name or self.user_mail

class Books(models.Model):
    book_name = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    book_author = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

   
    favorited_by = models.ManyToManyField(Users, through='UserBooks', related_name='favorite_books')

    def __str__(self):
        return self.book_name

class UserBooks(models.Model):
  
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    
 
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')