from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField('书名', max_length=30)
	author = models.CharField('作者', max_length=30)
	pub_date = models.DateTimeField('出版时间')
	price = models.IntegerField('价格')

	def __str__(self):
		return self.name

class Phone(models.Model):
	brand = models.CharField('品牌', max_length=30)
	number = models.CharField('号码', max_length=11)
	master = models.CharField('主人', max_length=30)
	price = models.IntegerField('价格')

	def __str__(self):
		return self.master