from django.contrib import admin
from .models import Book, Phone
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'pub_date', 'price') #显示的详情信息
	search_fields = ('name', 'author')   #可以按照名称或作者来搜索
	# list_filter = ('name',)  # 通过名称来过滤

class PhoneAdmin(admin.ModelAdmin):
	list_display = ('master', 'number', 'brand', 'price')
	search_fields = ('master', 'number')

admin.site.register(Book, BookAdmin)
admin.site.register(Phone, PhoneAdmin)


# 有时候我们需要对django admin site进行修改以满足自己的需求，那么我们可以从哪些地方入手呢？
# 以下举例说明：

# 1.定制加载的列表, 根据不同的人显示不同的内容列表，比如输入员只能看见自己输入的，审核员能看到所有的草稿，这时候就需要重写get_queryset方法
# class MyModelAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(MyModelAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(author=request.user)
# 该类实现的功能是如果是超级管理员就列出所有的，如果不是，就仅列出访问者自己相关的


# 2.定制搜索功能（django 1.6及以上才有)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age')
#     search_fields = ('name',)
 
#     def get_search_results(self, request, queryset, search_term):
#         queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
#         try:
#             search_term_as_int = int(search_term)
#             queryset |= self.model.objects.filter(age=search_term_as_int)
#         except:
#             pass
#         return queryset, use_distinct
# queryset 是默认的结果，search_term 是在后台搜索的关键词

# 3.修改保存时的一些操作，可以检查用户，保存的内容等，比如保存时加上添加人
# from django.contrib import admin
 
# class ArticleAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()
# 其中obj是修改后的对象，form是返回的表单（修改后的），当新建一个对象时 change = False, 当修改一个对象时 change = True
# 如果需要获取修改前的对象的内容可以用

# from django.contrib import admin
 
# class ArticleAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         obj_original = self.model.objects.get(pk=obj.pk)
#         obj.user = request.user
#         obj.save()
# 那么又有问题了，这里如果原来的obj不存在，也就是如果我们是新建的一个怎么办呢，这时候可以用try,except的方法尝试获取,当然更好的方法是判断一下这个对象是新建还是修改，是新建就没有 obj_original，是修改就有

# from django.contrib import admin
 
# class ArticleAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if change:# 更改的时候
#             obj_original = self.model.objects.get(pk=obj.pk)
#         else:# 新增的时候
#             obj_original = None
 
#         obj.user = request.user
#         obj.save()
# 4, 删除时做一些处理,

# from django.contrib import admin
 
# class ArticleAdmin(admin.ModelAdmin):
#     def delete_model(self, request, obj):
#         """
#         Given a model instance delete it from the database.
#         """
#         # handle something here
#         obj.delete()
