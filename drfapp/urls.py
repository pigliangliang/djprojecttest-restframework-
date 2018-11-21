#author_by zhuxiaoliang
#2018-11-15 上午9:42

from django.urls import path,re_path,include
#from .views import snippet_list,snippet_detail

#from .views import SnippetView,SnippetDetail,UserDetail,UserList,CreateUser,UserList2
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from .views import UserViewSet,SnippetViewSet



app_name = 'drfapp'


router =routers.DefaultRouter()
router.register(r'snippets',SnippetViewSet)
router.register(r'users',UserViewSet)

urlpatterns =[
    path(r'',include(router.urls)),





]

