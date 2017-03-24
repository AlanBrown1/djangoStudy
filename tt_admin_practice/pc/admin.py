from django.contrib import admin

from .models import Computer, Book
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
	list_display = ('name', 'master', 'brand','price', 'screen_size')
	list_filter = ('screen_size', 'brand')

class BookAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'price', 'status')
	list_filter = ('status',)

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Book, BookAdmin)
