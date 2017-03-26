from django.shortcuts import render
 
 
def home(reuqest):
    return render(reuqest, 'blog/index.html')
 
 
def columns(request):
    return render(request, 'blog/columns.html')