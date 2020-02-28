from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tut,TutCategory,TutSeries
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm




def single_slug(request,single_slug):
	categories = [c.category_slug for c in TutCategory.objects.all()]
	if single_slug in categories:
		matching_series = TutSeries.objects.filter(tut_category__category_slug=single_slug)
		
		series_urls = {}
		for m in matching_series.all():
			part_one = Tut.objects.filter(tut_series__tut_series=m.tut_series).earliest("tut_published")

			series_urls[m] = part_one.tut_slug



		return render(request, 
					  "main/category.html", 
					  {"part_ones": series_urls})

	tutorials = [t.tut_slug for t in Tut.objects.all()]
	if single_slug in tutorials:
		this_tutorial = Tut.objects.get(tut_slug= single_slug)

		return render(request,
					  "main/tutorial.html",
					  {"tutorial":this_tutorial})

		#return HttpResponse(f"{single_slug} is a tutorial!!!")

	return HttpResponse(f"{single_slug} does not correspond to anything!!!")


# Create your views here.
def homepage(request):
	return  render(request=request,
				   template_name="main/categories.html",
				   context={"categories": TutCategory.objects.all})

	#return HttpResponse("Hoping Django Will be <strong>Awesome</strong>")




#registration method
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account created: {username}")
			login(request,user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")

		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")
				

	form = NewUserForm
	return render(request,
				  "main/register.html",
				   context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "User Logged out")
	return redirect("main:homepage")



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				messages.info(request,f"You are logged-in as: {username}")
				return redirect("main:homepage")

			else:
				messages.error(request,"Invalid username or password")

		else:
				messages.error(request,"Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})

