from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^add/$',cart_add,name='add'),
	url(r'^count',cart_count,name='count'),
	url(r'^$',cart_show,name='show'),
	url(r'^del/$',cart_del,name='delete'),
	url(r'^update/$',cart_update,name='update'),
]