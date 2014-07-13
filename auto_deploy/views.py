from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from fabfile import auto_deploy

def home(request):
    deployed = False
    try:
        auto_deploy()
        deployed = True
    except:
        e = sys.exc_info()
        print e
    finally:
        return HttpResponse('Deployed: %s' %deployed)
