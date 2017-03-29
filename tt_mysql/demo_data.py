from blog.models import Book as bo, Author as au

def main():
	for i in range(1,21):
		name = '书名_' + str(i)
		author = '作者_' + str(i)
		word = 500*i
		bo.objects.get_or_create(name=name, author=author, wordcount=word)

	for i in range(1,10):
		name = '作者_' + str(i)
		age = 20 + i
		phone = '1234567891' + str(i)
		address = '北京市海淀区成府路29号'
		au.objects.get_or_create(name=name, age=age, phone=phone, address=address)


if __name__ == '__main__':
	main()
	print('Done !')