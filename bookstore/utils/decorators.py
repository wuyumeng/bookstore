from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse

def login_require(view_func):
	"""登录判断装饰器"""
	def wrapper(request,*args,**kwargs):
		if request.session.has_key('islogin'):
			return view_func(request,*args,**kwargs)
		else:
			return redirect(reverse('users:login'))
	return wrapper
