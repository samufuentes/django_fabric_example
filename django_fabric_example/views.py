from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')
