# from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render,redirect, get_object_or_404
from moviemanager.models import *
from .forms import *
from random import randrange


# Create your views here.
def home(request):
    movie = Movies.objects
    return render(request, 'home.html', {'movie': movie})

def detail(request, movie_id):
    moviedetail = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'detail.html', {'movie':moviedetail})

def book(request):
    rand = randrange(10000, 50000)
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "checkout.html", {"form": form, 'rand':rand})
    else:
        form = BookingsForm()
    return render(request, "book.html", {"form":form, 'rand':rand})

def checkout(request):
    return render(request, 'checkout.html')


def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')
