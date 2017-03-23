from django.db import models
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_models.settings")# project_name 项目名称
django.setup()

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name