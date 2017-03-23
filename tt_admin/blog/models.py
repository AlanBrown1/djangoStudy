from django.db import models
import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_admin.settings")# project_name 项目名称
# django.setup()
# # Create your models here.

class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    status = models.CharField('状态', max_length=3)
    #下面这个__str__函数是在后台管理界面把文章标题显示出来的
    #没有的话，文章标题就是 Article object，这样就不知道是哪篇文章了
    def __str__(self):
    	return self.title

class Person(models.Model):
	first_name = models.CharField('名', max_length=30)
	last_name = models.CharField('姓', max_length=30)

	def my_property(self):
		return self.first_name + ' ' + self.last_name
	my_property.short_description = '全名'

	full_name = property(my_property)