from django.db import models
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_admin_practice.settings")# project_name 项目名称
# django.setup()
# Create your models here.
class Computer(models.Model):
	name = models.CharField('名称', max_length=30)
	master = models.CharField('主人', max_length=30)
	brand = models.CharField('品牌', max_length=30)
	price = models.IntegerField('价格')
	screen_size = models.FloatField('屏幕尺寸')

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField('书名', max_length=50)
	author = models.CharField('作者', max_length=30)
	price = models.IntegerField('价格')
	status = models.CharField('状态', max_length=3)

	def __str__(self):
		return self.name