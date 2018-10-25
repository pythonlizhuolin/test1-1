#coding=utf-8
from django.http import HttpResponse


def student_urls(request):
    return HttpResponse('hello login')


def index_view(request):
    return HttpResponse('hello index')