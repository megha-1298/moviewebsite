from django.urls import path
from . import views


urlpatterns = [

    # path('profile/', views.profile, name='profile'),
    # path('', views.index, name='index'),
    # path('search/', views.search_movies, name='search_movies'),
    # # Add other paths for movies, categories, etc.

    path('',views.home,name='index'),
    path('details/<int:id>/',views.details,name="details"),
    path('add_movies/',views.add_movies,name="add_movies"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('add_review/<int:id>/',views.add_review,name="add_review"),
    path('edit_review/<int:movie_id>/<int:review_id>/',views.edit_review,name="edit_review"),
    path('delete_review/<int:movie_id>/<int:review_id>/',views.delete_review,name="delete_review"),
    path('',views.category,name="category"),
]



