from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .serializers import SnippetSerializers
from .models import Snippet
from django.http import QueryDict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import CreateUserSeiralizers

from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework import serializers

"""
django 不能友好的支持put，patch方法，使用api_view装饰器，即可使用request.data
"""

"""
def snippet_list(request):
    if request.method=="GET":
        snippet = Snippet.objects.all()
        serializers = SnippetSerializers(snippet,many=True)
        return JsonResponse(serializers.data,safe=False)

    elif request.method=="POST":
        data =request.POST
        print(data)
        serializers = SnippetSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=200)
        return JsonResponse(serializers.errors,status=400)




@api_view(['GET','DELETE','PATCH'])
def snippet_detail(request,id):
    snippet = Snippet.objects.get(id=id)
    if request.method=='GET':
        serializers = SnippetSerializers(snippet)
        return JsonResponse(serializers.data)

    elif request.method=='DELETE':
        snippet.delete()
        return JsonResponse('deleted ok')

    elif request.method=="PATCH":
        data = request.data
        serializers = SnippetSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=200)
        return JsonResponse(serializers.errors, status=400)
        #return HttpResponse('put func')

"""


"""
@api_view(['GET','POST'])
def snippet_list(request):
    if request.method=='GET':
        snippet = Snippet.objects.all()
        serializers = SnippetSerializers(snippet,many=True)
        return Response(serializers.data)
    elif request.method=='POST':
        print(request.data)
        data = request.data
        serializers = SnippetSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,id):
    try:
        snippet = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers = SnippetSerializers(snippet)
        return Response(serializers.data)

    elif request.method=='PUT':
        data = request.data
        serializers = SnippetSerializers(data=data,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


"""
#基于类的视图
class SnippetView(APIView):

    def get(self,request):

        snippet = Snippet.objects.all()
        serializers = SnippetSerializers(snippet,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = SnippetSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


class SnippetDetail(APIView):

    def get_object(self,id):
        try:
            snippet = Snippet.objects.get(id=id)
            print(snippet)
            return snippet
        except Snippet.DoesNotExist:
            return Http404
    def get(self,request,id):
        snippet = self.get_object(id)
        serializers = SnippetSerializers(snippet)
        return Response(serializers.data)

    def patch(self,request,id):
        snippet = self.get_object(id)
        serializers = SnippetSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        return Response(serializers.errors)
    def delete(self,id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(snippet)
        
"""


#基于mixin

"""
class SnippetView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):


    #必须重写下面两个方法，直接使用注释部门内容，报错
    #提示必须重写这两个方法

    def get_queryset(self):
        snippet = Snippet.objects.all()
        return snippet
    def get_serializer_class(self):
        serializer_class = SnippetSerializers
        return serializer_class

    # serializer_class = SnippetSerializers
    #
    # snippet = Snippet.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def create(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):


    #必须重写下面两个方法，直接使用注释部门内容，报错
    #提示必须重写这两个方法

    def get_queryset(self):
        snippet = Snippet.objects.all()
    def get_serializer_class(self):
        serializer_class = SnippetSerializers
        return serializer_class

    # serializer_class = SnippetSerializers
    #
    # snippet = Snippet.objects.all()

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""


#基于通用视图的类

""""
class SnippetView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

    #permissions = (permissions.IsAuthenticated,IsOwnerOrReadOnly)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()

    serializer_class = SnippetSerializers
    #permissions=(permissions.IsAuthenticated,IsOwnerOrReadOnly)

    # def perform_create(self,serializer):
    #     serializer.save()





class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers



class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSeiralizers

class UserList2(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSeiralizers
 """

#viewset


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  User.objects.all()

    serializer_class =UserSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers


