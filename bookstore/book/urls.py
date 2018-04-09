from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^book/(?P<books_id>\d+)/$',detail,name='detail'),
	url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$',list,name='list'),
]
