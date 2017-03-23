from __future__ import unicode_literals
 #这个__future__的导入必须放在第一个，作用是：Python提供了__future__模块，
 #把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。

 #django的数据库查询语句比SQL语句还复杂，麻烦
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_blog.settings")# project_name 项目名称
django.setup()
 
 
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()
 
    def __str__(self):
        return self.name
 
 
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')
 
    def __str__(self):
        return self.title
 
 
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name

# **********************************************************************
#  1. 查看 Django queryset 执行的 SQL
# In [1]: print str(Author.objects.all().query)
# SELECT "blog_author"."id", "blog_author"."name", "blog_author"."qq", "blog_author"."addr", "blog_author"."email" FROM "blog_author"
# 简化一下，就是：SELECT id, name, qq, addr, email FROM blog_author;

# In [2]: print str(Author.objects.filter(name="WeizhongTu").query)
# SELECT "blog_author"."id", "blog_author"."name", "blog_author"."qq", "blog_author"."addr", "blog_author"."email" FROM "blog_author" WHERE "blog_author"."name" = WeizhongTu
# 简化一下，就是：SELECT id, name, qq, addr, email FROM blog_author WHERE name=WeizhongTu;

# 所以，当不知道Django做了什么时，你可以把执行的 SQL 打出来看看，也可以借助 django-debug-toolbar 等工具在页面上看到访问当前页面执行了哪些SQL，耗时等。
# 还有一种办法就是修改一下 log 的设置，后面会讲到。

# **********************************************************************
# 2. values_list 获取元组形式结果
# 2.1 比如我们要获取作者的 name 和 qq

# In [6]: authors = Author.objects.values_list('name', 'qq')

# In [7]: authors
# Out[7]: <QuerySet [(u'WeizhongTu', u'336643078'), (u'twz915', u'915792575'), (u'wangdachui', u'353506297'), (u'xiaoming', u'004466315')]>

# In [8]: list(authors)
# Out[8]: 
# [(u'WeizhongTu', u'336643078'),
#  (u'twz915', u'915792575'),
#  (u'wangdachui', u'353506297'),
#  (u'xiaoming', u'004466315')]
# 如果只需要 1 个字段，可以指定 flat=True
# In [9]: Author.objects.values_list('name', flat=True)
# Out[9]: <QuerySet [u'WeizhongTu', u'twz915', u'wangdachui', u'xiaoming']>

# In [10]: list(Author.objects.values_list('name', flat=True))
# Out[10]: [u'WeizhongTu', u'twz915', u'wangdachui', u'xiaoming']

# 2.2 查询 twz915 这个人的文章标题
# In [11]: Article.objects.filter(author__name='twz915').values_list('title', flat=True)
# Out[11]: <QuerySet [u'HTML \u6559\u7a0b_1', u'HTML \u6559\u7a0b_2', u'HTML \u6559\u7a0b_3', u'HTML \u6559\u7a0b_4', u'HTML \u6559\u7a0b_5', u'HTML \u6559\u7a0b_6', u'HTML \u6559\u7a0b_7', u'HTML \u6559\u7a0b_8', u'HTML \u6559\u7a0b_9', u'HTML \u6559\u7a0b_10', u'HTML \u6559\u7a0b_11', u'HTML \u6559\u7a0b_12', u'HTML \u6559\u7a0b_13', u'HTML \u6559\u7a0b_14', u'HTML \u6559\u7a0b_15', u'HTML \u6559\u7a0b_16', u'HTML \u6559\u7a0b_17', u'HTML \u6559\u7a0b_18', u'HTML \u6559\u7a0b_19', u'HTML \u6559\u7a0b_20']>

# **********************************************************************
# 3. values 获取字典形式的结果
# 3.1 比如我们要获取作者的 name 和 qq

# In [13]: Author.objects.values('name', 'qq')
# Out[13]: <QuerySet [{'qq': u'336643078', 'name': u'WeizhongTu'}, {'qq': u'915792575', 'name': u'twz915'}, {'qq': u'353506297', 'name': u'wangdachui'}, {'qq': u'004466315', 'name': u'xiaoming'}]>

# In [14]: list(Author.objects.values('name', 'qq'))
# Out[14]: 
# [{'name': u'WeizhongTu', 'qq': u'336643078'},
#  {'name': u'twz915', 'qq': u'915792575'},
#  {'name': u'wangdachui', 'qq': u'353506297'},
#  {'name': u'xiaoming', 'qq': u'004466315'}]

# 3.2 查询 twz915 这个人的文章标题
# In [23]: Article.objects.filter(author__name='twz915').values('title')
# Out[23]: <QuerySet [{'title': u'HTML \u6559\u7a0b_1'}, {'title': u'HTML \u6559\u7a0b_2'}, {'title': u'HTML \u6559\u7a0b_3'}, {'title': u'HTML \u6559\u7a0b_4'}, {'title': u'HTML \u6559\u7a0b_5'}, {'title': u'HTML \u6559\u7a0b_6'}, {'title': u'HTML \u6559\u7a0b_7'}, {'title': u'HTML \u6559\u7a0b_8'}, {'title': u'HTML \u6559\u7a0b_9'}, {'title': u'HTML \u6559\u7a0b_10'}, {'title': u'HTML \u6559\u7a0b_11'}, {'title': u'HTML \u6559\u7a0b_12'}, {'title': u'HTML \u6559\u7a0b_13'}, {'title': u'HTML \u6559\u7a0b_14'}, {'title': u'HTML \u6559\u7a0b_15'}, {'title': u'HTML \u6559\u7a0b_16'}, {'title': u'HTML \u6559\u7a0b_17'}, {'title': u'HTML \u6559\u7a0b_18'}, {'title': u'HTML \u6559\u7a0b_19'}, {'title': u'HTML \u6559\u7a0b_20'}]>
# 注意：

# 1. values_list 和 values 返回的并不是真正的 列表 或 字典，也是 queryset，他们也是 lazy evaluation 的（惰性评估，通俗地说，就是用的时候才真正的去数据库查）

# 2. 如果查询后没有使用，在数据库更新后再使用，你发现得到在是新内容！！！如果想要旧内容保持着，数据库更新后不要变，可以 list 一下

# 3. 如果只是遍历这些结果，没有必要 list 它们转成列表（浪费内存，数据量大的时候要更谨慎！！！）


# **********************************************************************
# 4. extra 实现 别名，条件，排序等
# extra 中可实现别名，条件，排序等，后面两个用 filter, exclude 一般都能实现，排序用 order_by 也能实现。我们主要看一下别名这个

# 比如 Author 中有 name， Tag 中有 name 我们想执行

# SELECT name AS tag_name FROM blog_tag;

# 这样的语句，就可以用 select 来实现，如下：

# In [44]: tags = Tag.objects.all().extra(select={'tag_name': 'name'})

# In [45]: tags[0].name
# Out[45]: u'Django'

# In [46]: tags[0].tag_name
# Out[46]: u'Django'


# 我们发现 name 和 tag_name 都可以使用，确认一下执行的 SQL


# In [47]: Tag.objects.all().extra(select={'tag_name': 'name'}).query.__str__()
# Out[47]: u'SELECT (name) AS "tag_name", "blog_tag"."id", "blog_tag"."name" FROM "blog_tag"'


# 我们发现查询的时候弄了两次 (name) AS "tag_name" 和 "blog_tag"."name"

# 如果我们只想其中一个能用，可以用 defer 排除掉原来的 name （后面有讲）


# In [49]: Tag.objects.all().extra(select={'tag_name': 'name'}).defer('name').query.__str__()
# Out[49]: u'SELECT (name) AS "tag_name", "blog_tag"."id" FROM "blog_tag"'
# 也许你会说为什么要改个名称，最常见的需求就是数据转变成 list，然后可视化等，我们在下面一个里面讲。


# **********************************************************************
# 5. annotate 聚合 计数，求和，平均数等
# 5.1 计数

# 我们来计算一下每个作者的文章数（我们每个作者都导入的Article的篇数一样，所以下面的每个都一样）

# In [66]: from django.db.models import Count

# In [66]: Article.objects.all().values('author_id').annotate(count=Count('author')).values('author_id', 'count')
# Out[66]: <QuerySet [{'count': 20, 'author_id': 1}, {'count': 20, 'author_id': 2}, {'count': 20, 'author_id': 4}]>
# 这是怎么工作的呢？

# In [67]: Article.objects.all().values('author_id').annotate(count=Count('author')).values('author_id', 'count').query.__str__()
# Out[67]: u'SELECT "blog_article"."author_id", COUNT("blog_article"."author_id") AS "count" FROM "blog_article" GROUP BY "blog_article"."author_id"'
# 简化一下SQL: SELECT author_id, COUNT(author_id) AS count FROM blog_article GROUP BY author_id



# 我们也可以获取作者的名称 及 作者的文章数

# In [72]: Article.objects.all().values('author__name').annotate(count=Count('author')).values('author__name', 'count')
# Out[72]: <QuerySet [{'count': 20, 'author__name': u'WeizhongTu'}, {'count': 20, 'author__name': u'twz915'}, {'count': 20, 'author__name': u'xiaoming'}]>


# 这时候会查询两张表，细心的同学会发现，因为作者名称中 blog_author 这张表中，author_id 在 blog_article 表中本身就有的



# 5.2 求和 与 平均值

# 5.2.1 求一个作者的所有文章的得分(score)平均值

# In [6]: from django.db.models import Avg

# In [7]: Article.objects.values('author_id').annotate(avg_score=Avg('score')).values('author_id', 'avg_score')
# Out[7]: <QuerySet [{'author_id': 1, 'avg_score': 86.05}, {'author_id': 2, 'avg_score': 83.75}, {'author_id': 5, 'avg_score': 85.65}]>

# 执行的SQL
# In [8]: Article.objects.values('author_id').annotate(avg_score=Avg('score')).values('author_id', 'avg_score').qu
#    ...: ery.__str__()
# Out[8]: u'SELECT "blog_article"."author_id", AVG("blog_article"."score") AS "avg_score" FROM "blog_article" GROUP BY "blog_article"."author_id"'


# 5.2.2 求一个作者所有文章的总分

# In [12]: from django.db.models import Sum

# In [13]: Article.objects.values('author__name').annotate(sum_score=Sum('score')).values('author__name', 'sum_score')
# Out[13]: <QuerySet [{'author__name': u'WeizhongTu', 'sum_score': 1721}, {'author__name': u'twz915', 'sum_score': 1675}, {'author__name': u'zhen', 'sum_score': 1713}]>
# 执行的SQL

# In [14]: Article.objects.values('author__name').annotate(sum_score=Sum('score')).values('author__name', 'sum_sco
#     ...: re').query.__str__()
# Out[14]: u'SELECT "blog_author"."name", SUM("blog_article"."score") AS "sum_score" FROM "blog_article" INNER JOIN "blog_author" ON ("blog_article"."author_id" = "blog_author"."id") GROUP BY "blog_author"."name"'

# **********************************************************************
# 6.  select_related 优化一对一，多对一查询
# 开始之前我们修改一个 settings.py 让Django打印出在数据库中执行的语句

# settings.py 尾部加上
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG' if DEBUG else 'INFO',
#         },
#     },
# }
# 这样当 DEBUG 为 True 的时候，我们可以看出 django 执行了什么 SQL 语句


# tu@pro ~/zqxt $ python manage.py shell

# In [1]: from blog.models import *

# In [2]: Author.objects.all()
# Out[2]: (0.001) SELECT "blog_author"."id", "blog_author"."name", "blog_author"."qq", "blog_author"."addr", "blog_author"."email" FROM "blog_author" LIMIT 21; args=()
# <QuerySet [<Author: WeizhongTu>, <Author: twz915>, <Author: dachui>, <Author: zhe>, <Author: zhen>]>
# 标记背景为 黄色的部分就是打出的 log。

# 假如，我们取出10篇Django相关的文章，并需要用到作者的姓名

# In [13]: articles = Article.objects.all()[:10]

# In [14]: a1 = articles[0]  # 取第一篇
# (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score" FROM "blog_article" LIMIT 1; args=()

# In [15]: a1.title
# Out[15]: u'Django \u6559\u7a0b_1'

# In [16]: a1.author_id
# Out[16]: 5

# In [17]: a1.author.name   # 再次查询了数据库，注意！！！
# (0.000) SELECT "blog_author"."id", "blog_author"."name", "blog_author"."qq", "blog_author"."addr", "blog_author"."email" FROM "blog_author" WHERE "blog_author"."id" = 5; args=(5,)
# Out[17]: u'zhen'
# 这样的话我们遍历查询结果的时候就会查询很多次数据库，能不能只查询一次，把作者的信息也查出来呢？

# 当然可以，这时就用到 select_related，我们的数据库设计的是一篇文章只能有一个作者，一个作者可以有多篇文章。

# 现在要查询文章的时候连同作者一起查询出来，“文章”和“作者”的关系就是多对一，换句说说，就是一篇文章只可能有一个作者。

# In [18]: articles = Article.objects.all().select_related('author')[:10]

# In [19]: a1 = articles[0]  # 取第一篇
# (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score", "blog_author"."id", "blog_author"."name", "blog_author"."qq", "blog_author"."addr", "blog_author"."email" FROM "blog_article" INNER JOIN "blog_author" ON ("blog_article"."author_id" = "blog_author"."id") LIMIT 1; args=()

# In [20]: a1.title
# Out[20]: u'Django \u6559\u7a0b_1'

# In [21]: a1.author.name   # 嘻嘻，没有再次查询数据库！！
# Out[21]: u'zhen'

# **********************************************************************
# 7. prefetch_related 优化一对多，多对多查询
# 和 select_related 功能类似，但是实现不同。

# select_related 是使用 SQL JOIN 一次性取出相关的内容。

# prefetch_related 用于 一对多，多对多 的情况，这时 select_related 用不了，因为当前一条有好几条与之相关的内容。

# prefetch_related是通过再执行一条额外的SQL语句，然后用 Python 把两次SQL查询的内容关联（joining)到一起

# 我们来看个例子，查询文章的同时，查询文章对应的标签。“文章”与“标签”是多对多的关系。

# In [24]: articles = Article.objects.all().prefetch_related('tags')[:10]

# In [25]: articles
# Out[25]: (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score" FROM "blog_article" LIMIT 10; args=()
# (0.001) SELECT ("blog_article_tags"."article_id") AS "_prefetch_related_val_article_id", "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10); args=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# <QuerySet [<Article: Django 教程_1>, <Article: Django 教程_2>, <Article: Django 教程_3>, <Article: Django 教程_4>, <Article: Django 教程_5>, <Article: Django 教程_6>, <Article: Django 教程_7>, <Article: Django 教程_8>, <Article: Django 教程_9>, <Article: Django 教程_10>]>


# 遍历查询的结果：

# 不用 prefetch_related 时

# In [9]: articles = Article.objects.all()[:3]

# In [10]: for a in articles:
#     ...:     print a.title, a.tags.all()
#     ...:     
# (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score" FROM "blog_article" LIMIT 3; args=()

# (0.000) SELECT "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" = 1 LIMIT 21; args=(1,)

# Django 教程_1 <QuerySet [<Tag: Django>]>

# (0.000) SELECT "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" = 2 LIMIT 21; args=(2,)

# Django 教程_2 <QuerySet [<Tag: Django>]>

# (0.000) SELECT "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" = 3 LIMIT 21; args=(3,)

# Django 教程_3 <QuerySet [<Tag: Django>]>


# 用 prefetch_related 我们看一下是什么样子

# In [11]: articles = Article.objects.all().prefetch_related('tags')[:3]

# In [12]: for a in articles:
#    ...:     print a.title, a.tags.all()
#    ...:     
# (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score" FROM "blog_article" LIMIT 3; args=()
# (0.000) SELECT ("blog_article_tags"."article_id") AS "_prefetch_related_val_article_id", "blog_tag"."id", "blog_tag"."name" FROM "blog_tag" INNER JOIN "blog_article_tags" ON ("blog_tag"."id" = "blog_article_tags"."tag_id") WHERE "blog_article_tags"."article_id" IN (1, 2, 3); args=(1, 2, 3)
# Django 教程_1 <QuerySet [<Tag: Django>]>
# Django 教程_2 <QuerySet [<Tag: Django>]>
# Django 教程_3 <QuerySet [<Tag: Django>]>
# 我们可以看到第二条 SQL 语句，一次性查出了所有相关的内容。

# **********************************************************************
# 8. defer 排除不需要的字段
# 在复杂的情况下，表中可能有些字段内容非常多，取出来转化成 Python 对象会占用大量的资源。

# 这时候可以用 defer 来排除这些字段，比如我们在文章列表页，只需要文章的标题和作者，没有必要把文章的内容也获取出来（因为会转换成python对象，浪费内存）

# In [13]: Article.objects.all()
# Out[13]: (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."content", "blog_article"."score" FROM "blog_article" LIMIT 21; args=()
# <QuerySet [<Article: Django 教程_1>, <Article: Django 教程_2>, <Article: Django 教程_3>, <Article: Django 教程_4>, <Article: Django 教程_5>, <Article: Django 教程_6>, <Article: Django 教程_7>, <Article: Django 教程_8>, <Article: Django 教程_9>, <Article: Django 教程_10>, <Article: Django 教程_11>, <Article: Django 教程_12>, <Article: Django 教程_13>, <Article: Django 教程_14>, <Article: Django 教程_15>, <Article: Django 教程_16>, <Article: Django 教程_17>, <Article: Django 教程_18>, <Article: Django 教程_19>, <Article: Django 教程_20>, '...(remaining elements truncated)...']>

# In [14]: Article.objects.all().defer('content')
# Out[14]: (0.000) SELECT "blog_article"."id", "blog_article"."title", "blog_article"."author_id", "blog_article"."score" FROM "blog_article" LIMIT 21; args=()  # 注意这里没有查 content 字段了
# <QuerySet [<Article: Django 教程_1>, <Article: Django 教程_2>, <Article: Django 教程_3>, <Article: Django 教程_4>, <Article: Django 教程_5>, <Article: Django 教程_6>, <Article: Django 教程_7>, <Article: Django 教程_8>, <Article: Django 教程_9>, <Article: Django 教程_10>, <Article: Django 教程_11>, <Article: Django 教程_12>, <Article: Django 教程_13>, <Article: Django 教程_14>, <Article: Django 教程_15>, <Article: Django 教程_16>, <Article: Django 教程_17>, <Article: Django 教程_18>, <Article: Django 教程_19>, <Article: Django 教程_20>, '...(remaining elements truncated)...']>

# **********************************************************************
# 9. only 仅选择需要的字段
# 和 defer 相反，only 用于取出需要的字段，假如我们只需要查出 作者的名称

# In [15]: Author.objects.all().only('name')
# Out[15]: (0.000) SELECT "blog_author"."id", "blog_author"."name" FROM "blog_author" LIMIT 21; args=()
# <QuerySet [<Author: WeizhongTu>, <Author: twz915>, <Author: dachui>, <Author: zhe>, <Author: zhen>]>
# 细心的同学会发现，我们让查 name ， id 也查了，这个 id 是 主键，能不能没有这个 id 呢？

# 试一下原生的 SQL 查询

# In [26]: authors =  Author.objects.raw('select name from blog_author limit 1')

# In [27]: author = authors[0]
# (0.000) select name from blog_author limit 1; args=()
# ---------------------------------------------------------------------------
# InvalidQuery                              Traceback (most recent call last)
# <ipython-input-27-51c5f914fff2> in <module>()
# ----> 1author = authors[0]

# /usr/local/lib/python2.7/site-packages/django/db/models/query.pyc in __getitem__(self, k)
#    1275 
#    1276     def __getitem__(self, k):
# -> 1277         return list(self)[k]
#    1278 
#    1279     @property

# /usr/local/lib/python2.7/site-packages/django/db/models/query.pyc in __iter__(self)
#    1250             if skip:
#    1251                 if self.model._meta.pk.attname in skip:
# -> 1252                     raise InvalidQuery('Raw query must include the primary key')
#    1253             model_cls = self.model
#    1254             fields =[self.model_fields.get(c)for c in self.columns]

# InvalidQuery: Raw query must include the primary key
# 报错信息说 非法查询，原生SQL查询必须包含 主键！



# 再试试直接执行 SQL

# tu@pro ~/zqxt $ python manage.py dbshell
# SQLite version 3.14.0 2016-07-26 15:17:14
# Enter ".help" for usage hints.
# sqlite> select name from blog_author limit 1;
# WeizhongTu       <---  成功！！！
# 虽然直接执行SQL语句可以这样，但是 django queryset 不允许这样做，一般也不需要关心，反正 only 一定会取出你指定了的字段。


# **********************************************************************
# 10. 自定义聚合功能
# 我们前面看到了 django.db.models 中有 Count, Avg, Sum 等，但是有一些没有的，比如 GROUP_CONCAT，它用来聚合时将符合某分组条件(group by)的不同的值，连到一起，作为整体返回。

# 我们来演示一下，如果实现 GROUP_CONCAT 功能。

# 新建一个文件 比如 my_aggregate.py
# from django.db.models import Aggregate, CharField
 
 
# class GroupConcat(Aggregate):
#     function = 'GROUP_CONCAT'
#     template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'
 
#     def __init__(self, expression, distinct=False, ordering=None, separator=',', **extra):
#         super(GroupConcat, self).__init__(
#             expression,
#             distinct='DISTINCT ' if distinct else '',
#             ordering=' ORDER BY %s' % ordering if ordering is not None else '',
#             separator=' SEPARATOR "%s"' % separator,
#             output_field=CharField(),
#             **extra        )
# 代码来自：http://stackoverflow.com/a/40478702/2714931（我根据一个回复改写的增强版本）



# 使用时先引入 GroupConcat 这个类，比如聚合后的错误日志记录有这些字段 time, level, info

# 我们想把 level, info 一样的 聚到到一起，按时间和发生次数倒序排列，并含有每次日志发生的时间。

# ErrorLogModel.objects.values('level', 'info').annotate(
#     count=Count(1), time=GroupConcat('time', ordering='time DESC', separator=' | ')
# ).order_by('-time', '-count')