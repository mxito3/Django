# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-30 21:17:34
# @Last Modified by:   YP
# @Last Modified time: 2018-07-30 21:30:34
from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
	test1=Test(name='yapie')
	test1.save()
	return HttpResponse('<p>数据添加成功</p>') 