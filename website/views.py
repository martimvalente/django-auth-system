from django.shortcuts import render

# Create your views here.
def homepage(request):
	pagedata = {
	  "pagetitle": "MyFishingBuddy - Homepage",
	  "model": "Mustang",
	  "year": "1964"
	}
	return render(request, 'homepage.html', pagedata)

def register(request):
	return render(request,'register.html')