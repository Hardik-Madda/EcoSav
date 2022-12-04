from django import forms
from django.contrib.auth.models import User
from BloggingApp.models import AddPost1


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class AddPost1Form(forms.ModelForm):
    Name = forms.CharField(max_length=30)
    email = forms.EmailField()
    Write_Post = forms.TextInput()
    class Meta:
        model = AddPost1
        fields = ('Name', 'email', 'Write_Post', 'image')


