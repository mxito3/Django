# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-31 12:45:13
# @Last Modified by:   YP
# @Last Modified time: 2018-07-31 13:01:24
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		if request.GET['q'] is None:
			message='你提交了空表单'
		else:
			message='你搜索的内容为'+request.GET['q']
	else:
		message='表单中没有这个键'
		
	return HttpResponse(message)

