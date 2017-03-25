"""tt_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()
# autodiscover() load all admin.py from the apps folders. 
#So you have in the /admin/ all the models that you use (from your own app or not).
# I recommend to use autodiscover() if you are going to use the admin app.
# P.D. additionally some app have their on autodiscover with more functionalities.
from form1 import views as f_views

urlpatterns = [
	url(r'^$', f_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
