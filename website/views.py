from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homepage(request):
	pagedata = {
	  "pagetitle": "MyFishingBuddy - Homepage",
	  "model": "Mustang",
	  "year": "1964"
	}
	return render(request, 'homepage.html', pagedata)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    return render(request, "registration/register.html", {
        "form": form
    })