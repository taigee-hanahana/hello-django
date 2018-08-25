from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePageView(requset):
	return HttpResponse('Hello,World!')

