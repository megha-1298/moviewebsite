#
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Movie
# from .models import UserProfile
#
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput())
#
#
# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']
#
#

from django import forms
from .models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=('title','actors','description','release_date','image','category')

class ReviewForm(forms.ModelForm):
    class Meta:
        model =Review
        fields=("comment","rating")
#)