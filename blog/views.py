from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starging_page(request):
    return HttpResponse('starging_page')

def posts(request):
    return HttpResponse('posts')

def post_detail(request):
     return HttpResponse('post_detail')

