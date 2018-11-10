from django.shortcuts import render,render_to_response
from .models import BBS,Category
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect



def index(request):
    bbs_list = BBS.objects.all()
    bbs_categories = Category.objects.all()
    return render_to_response('index.html', {
        'bbs_list': bbs_list,
        'user': request.user,
        'bbs_category': bbs_categories,
        'cata_id': 0})


def bbs_detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs, 'user': request.user})


def category_item(request,category_id):
    category_content = BBS.objects.filter(category__id=category_id)
    print(category_content)
    return render_to_response('categorycotents.html',{'category_obj':category_content})

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            render_to_response('login.html')
    else:
        return render_to_response('login.html')


def acc_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render_to_response('login.html', {'login_err': 'Wrong username or password!'})


def loginout(request):
    auth.logout(request)
    return  HttpResponse('thank you {}'.format(request.user))