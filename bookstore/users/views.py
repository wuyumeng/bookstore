from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import re
from .models import Passport,Address
from django.http import JsonResponse
from utils.decorators import login_require
# Create your views here.


def register(request):
	return render(request,'users/register.html')


def register_handle(request):
	"""用户注册处理"""
	#接受用户表单数据
	username = request.POST.get("user_name")
	password = request.POST.get("pwd")
	email = request.POST.get("email")

	#进行数据校验
	if not all([username,password,email]):
		#有数据为空
		return render(request,'users/register.html',{"errmsg":"参数不能为空"})
	#判断邮箱是否合法
	if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
		#邮箱不合法
		return render(request,'users/register.html',{"errmsg":"邮箱不合法"})
	#写入数据库
	Passport.objects.add_one_passport(username=username,password=password,email=email)
	#因为重写了Manage方法所以也可以这样写
	# passport = Passport.objects.add_one_passport(username=username,password=password,email=email)
	return redirect(reverse('book:index'))

def login(request):
	"""显示登录页面"""
	username = ''
	checked = ''
	context = {
		'username':username,
		'checked':checked,
	}
	return render(request,'users/login.html',context)

def login_check(request):
	"""进行登录校验"""
	username = request.POST.get("username")
	password = request.POST.get("password")
	remember = request.POST.get("remember")


	passport = Passport.objects.get_one_passport(username=username,password=password)
	if passport:
		if request.session.has_key('url_path'):
			next_url = request.session.get("url_path")
		else:
			next_url = reverse('book:index')
		next_url = request.session.get('url_path',reverse('book:index'))
		jres = JsonResponse({'res':1,'next_url':next_url})


		if remember == 'true':
			jres.set_cookie('username',username,max_age=7*24*3600)
		else:
			jres.delete_cookie('username')

		request.session['islogin'] = True
		request.session['username'] = username
		request.session['passport_id'] = passport.id
		return jres
	else:
		return JsonResponse({'res':0})


def logout(request):
	request.session.flush()
	return redirect(reverse('book:index'))


@login_require
def user(request):
	"""用户中心---信息页"""
	passport_id = request.session.get("passport_id")
	addr = Address.objects.get_default_address(passport_id=passport_id)
	books_li = []
	context = {
		'addr':addr,
		'page':'user',
		'books_li':books_li
	}
	return render(request,'users/user_center_info.html',context)

