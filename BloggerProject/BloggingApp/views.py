
from django.contrib.auth.decorators import login_required
from BloggingApp.forms import SignUpForm
from BloggingApp.forms import AddPost1Form
from django.shortcuts import render
import time
import datetime
from BloggingApp.models import AddPost1
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

# Create your views here.

def home_page_view(request):
    date2 = time.ctime()
    date1 = datetime.datetime.now()
    print(date1)
    return render(request, 'BloggingApp/addpost1_detail.html', {"server_datetime": date1, "server_datetime2": date2})

def signup_view(request):
    formobj = SignUpForm()
    if request.method == "POST":
        formobj = SignUpForm(request.POST)
        user = formobj.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'BloggingApp/signup.html', {'formobj': formobj})

class AddPost1ListView(ListView):
    model = AddPost1

class AddPost1DetailView(DetailView):
    model = AddPost1

class AddPost1CreateView(CreateView):
    model = AddPost1
    fields = ('Name', 'email', 'Write_Post')

def add_post_view(request):
    date2 = time.ctime()
    date1 = datetime.datetime.now()
    print(date1)
    formObj = AddPost1Form()
    if request.method == "POST":
        formObj = AddPost1Form(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['name'])
            print(formObj.cleaned_data['write_post'])
            formObj.save()
    post_list = AddPost1.objects.all()
    return render(request, 'BloggingApp/addpost1_form.html', {"post_list": post_list, "server_datetime": date1, "server_datetime2": date2})

def logout_view(request):
    date2 = time.ctime()
    date1 = datetime.datetime.now()
    print(date1)
    return render(request, 'BloggingApp/logout.html', {"server_datetime": date1, "server_datetime2": date2})

