# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-30 21:17:34
# @Last Modified by:   YP
# @Last Modified time: 2018-07-31 11:34:00
from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
	# test1=Test(name='yapie')
	# test1.save()
	#return HttpResponse('<p>数据添加成功</p>') 
	#
	#
	#修改数据
			#第一种方式
	# test2=Test.objects.get(id=1)
	# test2.name='mxito3'
	# test2.save()
	#		第二种方式
	#test2=Test.objects.filter(id=1).update(name='yapie')
	#删除数据
	#return HttpResponse('<h1>数据修改成功</h1>')
	#第一种方式
	# test3=Test.objects.get(id=1)
	# test3.delete()
	Test.objects.filter(id=3).delete()
	return HttpResponse('<h1>数据删除成功</h1>')