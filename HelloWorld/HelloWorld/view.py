# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-30 17:42:31
# @Last Modified by:   YP
# @Last Modified time: 2018-07-30 18:01:17
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
	context = {}
	context['hello']="hello world"
	return render(request,"helloworld.html")