from django.db import models
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_mysql.settings")# project_name 项目名称
django.setup()
# Create your models here.
class Book(models.Model):
	name = models.CharField('书名', max_length=50)
	author = models.CharField('作者', max_length=30)
	wordcount = models.IntegerField('字数')

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField('姓名', max_length=30)
	age = models.IntegerField('年龄')
	phone = models.CharField('电话', max_length=11)
	address = models.CharField('地址', max_length=50, default='湖北省武汉市')

	def __str__(self):
		return self.name