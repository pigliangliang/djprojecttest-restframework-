#author_by zhuxiaoliang
#2018-11-15 上午12:01

from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User
#
# class SnippetSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100,required=True,allow_blank=True)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     lineos = serializers.BooleanField(required=True)
#     language = serializers.CharField(default='Python')
#     style = serializers.CharField(default='friendly')
#
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'owner',
                  'title', 'code', 'language', 'styles')

class UserSerializers(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    #snippets = serializers.HyperlinkedRelatedField(many=True, view_name='drfapp:snippet-detail', read_only=True)
    class Meta:
        model =User
        fields = ('username', 'snippets')



class CreateUserSeiralizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username','email')