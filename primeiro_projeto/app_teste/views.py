from django.shortcuts import render, HttpResponse

def index(resquest):
    return HttpResponse('Hello World!')
