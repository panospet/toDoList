"""myToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from rest_framework import routers
from toDoList import views
from django.contrib.auth import views as auth_views

task_router = routers.DefaultRouter()
task_router.register(r'tasks', views.TaskViewSet, base_name='tasks')

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/', include(task_router.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
]
