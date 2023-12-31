from django.shortcuts import render, redirect

from django.urls import reverse
from .models import Advertisement
from django.http import HttpResponse
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "index.html", context=context)


def top(request):
    return render(request, 'top-sellers.html')


def post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.users
            advertisement.save()
            url = reverse("/")
            return redirect(url)
        else:
            form = AdvertisementForm()
        context = {"form": form}
        return render(request, "advertisement-post.html", context=context)


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


def advertisement(request):
    return render(request, "advertisement.html")
