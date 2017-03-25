from django.db import models
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_import.settings")# project_name 项目名称
django.setup()

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.title


# 往数据库批量导入数据时，可以把源数据放在项目中，然后在项目中新建一个用于执行导入的py文件
# 里面执行从源数据获取数据，然后执行导入的功能。
# 比如这个例子，在项目路径下面放了一个oldblog.txt记事本，里面的title和content用四个*号隔开
# 然后新建了一个txt2db.py文件，用来解析获取数据并执行导入数据库。