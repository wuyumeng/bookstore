from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^register/$',register,name='register'),
	url(r'^register_handle/$',register_handle,name='register_handle'),
	url(r'^login/$',login,name='login'),
	url(r'^login_check/$',login_check,name='login_check'),
	url(r'^logout/$',logout,name='logout'),
	url(r'^$',user,name='user'),
]