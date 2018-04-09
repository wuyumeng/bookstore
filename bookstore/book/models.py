from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
from book.enums import *



class BookManage(models.Manager):
	def get_book_by_type(self,type_id,limit=None,sort='default'):
		"""根据商品类型ID进行查询"""
		if sort == 'new':
			order_by = ('-create_time',)
		elif sort == 'hot':
			order_by = ('-sales',)
		elif sort == 'price':
			order_by = ('price',)
		else:
			order_by = ('-pk',)
		#查询数据
		books_li = self.filter(type_id=type_id).order_by(*order_by)

		#查询结果集的限制

		if limit:
			books_li = books_li[:limit]
		return books_li
	def get_book_by_id(self,book_id):
		"""根据商品的ID进行查询"""
		try:
			book = self.get(id=book_id)
		except self.model.DoesNotExist:
			#商品信息不存在
			book = None
		return book


class Books(BaseModel):
	"""商品模型类"""
	books_type_choices = ((k,v) for k,v in BOOKS_TYPE.items())
	status_choice = ((k,v) for k,v in STATUS_CHOICE.items())
	type_id = models.SmallIntegerField(default=PYTHON,choices=books_type_choices,verbose_name='商品种类')
	name = models.CharField(max_length=20,verbose_name='商品名称')
	desc = models.CharField(max_length=128,verbose_name='商品简介')
	price = models.DecimalField(max_length=10,max_digits=5,decimal_places=2,verbose_name='商品价格')
	unit = models.CharField(max_length=20,verbose_name='商品单位')
	stock = models.IntegerField(default=1,verbose_name='商品库存')
	sales = models.IntegerField(default=0,verbose_name='商品销量')
	detail = HTMLField(verbose_name='商品详情')
	image = models.ImageField(upload_to='books',verbose_name='商品图片')
	status = models.SmallIntegerField(default=ONLINE,choices=status_choice,verbose_name='商品状态')

	objects = BookManage()

	class Meta:
		verbose_name = '书籍'
		db_table = 's_books'
		verbose_name_plural = verbose_name
