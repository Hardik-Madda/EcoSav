
from django.contrib.auth.decorators import login_required
from BloggingApp.forms import SignUpForm, CommentForm, EmailSendForm
from BloggingApp.forms import AddPost1Form
import time
import datetime
from BloggingApp.models import AddPost1, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home_page_view(request,addpost1):
    date2 = time.ctime()
    date1 = datetime.datetime.now()
    print(date1)
    post = get_object_or_404(AddPost1)
    comments = addpost1.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()
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
    paginate_by = 1

def post_list_view(request):
    post_list = AddPost1.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'BloggingApp/addpost1_list.html', {"post_list":post_list})

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

def mail_send_view(request,id):
    post = get_object_or_404(AddPost1,id=id, status='published')
    sent = False
    if request.method =='POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}({}) recommends you to read "{}"'.format(cd['username'], cd['email'],	post.Name)
            message = "Read Post At: \n{}\n\n{} 'Comments:\n{}".format(post_url,cd['name'], cd['comments'])
            send_mail(subject, message, 'dawghardik@gmail.com', cd['to'])
            sent = True
    else:
        form = EmailSendForm()
    return render(request, 'BloggingApp/sharebymail.html', {'post': post, 'form': form, 'sent': sent})

def logout_view(request):
    date2 = time.ctime()
    date1 = datetime.datetime.now()
    print(date1)
    return render(request, 'BloggingApp/logout.html', {"server_datetime": date1, "server_datetime2": date2})

