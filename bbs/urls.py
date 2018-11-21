#author_by zhuxiaoliang
#2018-11-08 下午4:16

from django.urls import path,re_path
from .views import index,bbs_detail,category_item,acc_login,login,loginout

urlpatterns = [

    re_path(r'^$',index),
    re_path(r'^detail/(\d+)',bbs_detail),
    re_path(r'category/(\d+)',category_item),
    path('acc_login/',acc_login),
    path('login/',login),
    path('logout/',login)

]
