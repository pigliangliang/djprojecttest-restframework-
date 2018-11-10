#author_by zhuxiaoliang
#2018-11-10 下午12:10
from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    headimage = forms.FileField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()