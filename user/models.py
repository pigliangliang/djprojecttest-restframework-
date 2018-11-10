from django.db import models

# Create your models here.
#上传文件,文件内容保存在upload_to 目录中，数据库中保存的文件的路径。
class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64,null=False,unique=True)
    password = models.CharField(max_length=128,null=False)
    headimage  = models.FileField(upload_to='upload/',default='upload/1.jpg')
    def __str__(self):
        return "{} {}".format(self.name,self.id)

class Author(models.Model):
    name = models.CharField(max_length=64)


    def __str__(self):
        return "{} {}".format(self.name,self.id)

class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name