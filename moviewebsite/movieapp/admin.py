# from django.contrib import admin
#
# # Register your models here.
#
#
# from django.contrib import admin
#
# from . models import Movie
# from . models import Review
# from .models import Movie, Category
#
# admin.site.register(Movie)
# admin.site.register(Review)
# admin.site.register(Category)


from django.contrib import admin
from . models import *

#Register your models here
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Category)