from django.contrib import admin
from .models import Article, Person
# Register your models here.

# 下面这个类是用来使后台管理界面显示文章的其它信息的
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'content','pub_date','update_time', 'status')  # 变量名就是list_display，不要改。可以是('title', 'content',)，最后的逗号可有可无
	list_filter = ('status',)  # 可以通过文章的状态来进行过滤

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name','first_name' ,'last_name')

admin.site.register(Article, ArticleAdmin) # 然后把Article这个表和ArticleAdmin一起注册
admin.site.register(Person, PersonAdmin)