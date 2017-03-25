"""tt_ajax URL Configuration

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

from blog import views as b_views

urlpatterns = [
	url(r'^$', b_views.home),
	url(r'^home/$', b_views.home, name='home'),
	url(r'^add/$', b_views.add, name='add'),
	url(r'^ajax_list/$', b_views.ajax_list, name='ajax_list'),
	url(r'^ajax_dict/$', b_views.ajax_dict, name='ajax_dict'),
    url(r'^admin/', admin.site.urls),
]
