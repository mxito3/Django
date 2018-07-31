# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-31 13:04:47
# @Last Modified by:   YP
# @Last Modified time: 2018-07-31 13:21:15
from django.shortcuts import render
from django.views.decorators import csrf

def search(request):
	ctx={}
	if request.POST:
		ctx['rlt']=request.POST['q']
	return render(request,'search_in_post.html',ctx) 
