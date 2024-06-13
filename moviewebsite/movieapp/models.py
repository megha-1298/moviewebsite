# from django.db import models
# from django.contrib.auth.models import User
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Movie(models.Model):
#     objects = None
#     title = models.CharField(max_length=200)
#     poster = models.ImageField(upload_to='posters/')
#     description = models.TextField()
#     release_date = models.DateField()
#     actors = models.CharField(max_length=300)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     trailer_link = models.URLField()
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     review_text = models.TextField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.user.username} review of {self.movie.title}'


from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=300)
    trailer_link = models.URLField()
    average_rating=models.IntegerField(default=0.0)
    image= models.URLField(default=None,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=None,null=True,blank=True)  # Added category field



    def __str__(self):
        return self.title

class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=1000,default=None)
    rating= models.FloatField(default=0)

    def __str__(self):
        return self.user.username


