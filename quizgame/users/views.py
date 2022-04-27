from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewUserForm
from django.contrib import messages

result = 0

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("users:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"register_form":form})

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method =="POST":
        username = request.POST["mail"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out."
    })

def ques2(request):
    if request.GET:
        ans = request.POST.get("ans1")
        if ans == 28:
            global result
            result += 1
        return render(request, "users/ques2.html")

def ques3(request):
    if request.GET:
        ans = request.POST.get("ans2")
        ans = str(ans
        if ans.lower() in ["delhi"]:
            global result
            result +=1
        return render(request, "users/result.html")

def result(request):
    global result
    return render(request, "users/result.html", {
        "Score": result
    })
