#author_by zhuxiaoliang
#2018-11-10 下午12:10
from django import forms
from django.forms import fields
class UserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    headimage = forms.FileField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class LoginForm(forms.Form):
    name = fields.CharField(max_length=10,
                            min_length=6,
                            required=True,
                            error_messages={
                                'required':'必填字段',
                                'min_length':'最少6个字符',
                                'max_length':'最多10个字符',
                            }
                            )
    pwd = fields.CharField(min_length=3,
                           required=True,
                           error_messages={
                               'required': '密码不能为空',  # error_messages参数 自定义错误信息
                               'min_length': '太短了',
                               'max_length': "太长了",
                           }

                           )