import django

# 1  ******************************************************************************
# def main():
# 	from blog.models import Blog
# 	f = open('oldblog.txt')
# 	for line in f:
# 		title, content = line.split('****')
# 		Blog.objects.create(title = title , content = content)
# 		#为了避免数据重复，可以使用Blog.objects.get_or_create()
# 		#这个函数先判断数据库中是否存在该数据，没有的就create，有的话就不添加
# 		#该函数返回(BlogOject, True/False)，新建了就是True,已经存在就是False
# 	f.close()



# 2  ******************************************************************************
#由于Blog.objects.create()每保存一条就执行一次SQL，
#而bulk_create()是执行一条SQL存入多条数据，做会快很多！
def main():
	from blog.models import Blog as bl
	f = open('oldblog.txt')
	bloglist = []
	for i in f:
		title, content = i.split('****')
		b = bl(title=title, content=content)
		bloglist.append(b)
	f.close()
	# 上面这个for，使用列表生成式会更快一些
	# bloglist = [ bl(title=i.split('****')[0], content=i.split('****')[1]) for i in f ]
	bl.objects.bulk_create(bloglist)




if __name__ == '__main__':
	main()
	print('Done!!!')



