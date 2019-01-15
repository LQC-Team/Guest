from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
import urllib.request
#post
from django.template import RequestContext

# Create your views here.
# def login(request):
#     return render(request,"login.html")
# def login_action(request):
#     if request.method=="POST":
#         username = request.POST.get('username','')
#         password = request.POST.get('password','')
#         if username == 'admin' and password == 'admin':
#             return HttpResponseRedirect('/event_manage/')
#         else:
#             return render(request,'login.html',{'error':'username or password error'})

def index(request):

    return render(request, 'index.html')


    
    