
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from  django.db.models import Avg
# def home(request):
#     query = request.GET.get("title")
#     category_filter = request.GET.get("category")
#     if request.user.is_authenticated:
#
#
#         categories = Category.objects.all()
#         allMovies=Movie.objects.all()
#
#     if query:
#         allMovies =Movie.objects.filter(title__icontains=query)
#     if category_filter:
#         allMovies = Movie.objects.filter(category__name__icontains=category_filter)
#
#
#     else:
#          allMovies = Movie.objects.all()
#     context={"movies":allMovies,
#              "categories":categories,
#
#              }
#
#     return render(request,'index.html',context)


def home(request):
    query = request.GET.get("title", "")
    category_filter = request.GET.get("category", "")

    # Get all categories
    categories = Category.objects.all()

    # Start with all movies
    allMovies = Movie.objects.all()

    # Apply filters
    if query:
        allMovies = allMovies.filter(title__icontains=query)
    if category_filter:
        allMovies = allMovies.filter(category__name__icontains=category_filter)

    # Prepare context
    context = {
        "movies": allMovies,
        "categories": categories,
        "query": query,
        "category_filter": category_filter,
    }

    return render(request, 'index.html', context)

def details(request,id):
    movie=Movie.objects.get(id=id)
    reviews=Review.objects.filter(movie=id).order_by("-comment")

    average= reviews.aggregate(Avg("rating")).get("rating__avg",0)
    if average==None:
        average=0
    average=round(average,2)

    context={
        "movie":movie,
        "reviews":reviews,
        "average":average

    }

    return render( request,'details.html', context)

def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=="POST":
                form=MovieForm(request.POST or None)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect('index')

            else:
                form =MovieForm()
            return render(request,'add_movies.html',{'form':form, "controller":"Add Movies"})
        else:
            return redirect("index")

    return redirect("accounts:login")


def edit(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie=Movie.objects.get(id=id)

            if request.method == "POST":
                form=MovieForm(request.POST or None,instance=movie)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('details',id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'add_movies.html', {'form': form,"controller":"Edit Movies"})
        else:
            return redirect("index")

    return redirect("accounts:login")

def delete(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie=Movie.objects.get(id=id)

            movie.delete()
            return redirect("index")
        else:
            return redirect("index")

    return redirect("accounts:login")

def add_review(request,id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)

            if form.is_valid():
                data=form.save(commit=False)
                data.comment=request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("details",id)
        else:
            form =ReviewForm
        return redirect( request,"details.html", {"form":form})
    else:
        return redirect("accounts:login")

def edit_review(request,movie_id,review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review =Review.objects.get(movie=movie,id=review_id)

        if request.user == review.user:
            if request.method=="POST":
                form=ReviewForm(request.POST,instance=review)
                if form.is_valid():
                    data=form.save(commit=False)
                    if (data.rating >10) or (data.rating <0):
                        error="Out of range. Please select rating from 0 to 10"
                        return render(request,'edit_review.html',{"error":error,"form":form})
                    else:
                        data.save()
                        return redirect("details",movie_id)
            else:
                form=ReviewForm(instance=review)
            return render(request,"edit_review.html",{"form":form})
        else:
            return redirect("details",movie_id)
    else:
        return redirect("accounts:login")


def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            review.delete()

        return redirect("details", movie_id)
    else:
        return redirect("accounts:login")



def category(request):
    if request.user.is_authenticated:
        category_filter = request.GET.get("category")
        categories = Category.objects.all()

        if category_filter:
            allMovies = Movie.objects.filter(category__name__icontains=category_filter)
        else:
            allMovies = Movie.objects.all()

        # Prepare the context for the template
        context = {
            "movies": allMovies,
            "categories": categories,
        }

        # Render the template with the context
        return render(request, 'index.html', context)

    # Redirect to login page if the user is not authenticated
    return redirect('login')








