from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def homepage(request):
	pagedata = {
	  "pagetitle": "MyFishingBuddy - Homepage"
	}
	return render(request, 'homepage.html', pagedata)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST) #using django's auth library
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    return render(request, "registration/register.html", {
        "form": form    
    })

@login_required
def panel(request):
	pagedata = {
	  "pagetitle": "My Panel"
	}
	return render(request, 'panel.html', pagedata)
