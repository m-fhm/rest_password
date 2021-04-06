from django.shortcuts import render,redirect
from django.template.loader import render_to_string
import requests
import json

# Create your views here.
from django.http import HttpResponse


def index1(request):
    return HttpResponse("Hello, world. You're at the dashboard_csr index.")

def index(request):
    # print(request.headers)
    title = 'Reports'
    code = 'X3'
    info1 = request.GET
    info2 = request.POST
    info3 = request.COOKIES
    info4 = request.META
    info5 = request.FILES
    info6 = request.path
    method = request.method
    html = render_to_string('dashboard_csr.html', {'method': method, 'title': title, 'code': code, 'info1': info1, 'info2': info2, 'info3': info3, 'info4': info4, 'info5': info5, 'info6': info6})
    return HttpResponse(html)




def user_password_rest_through_dashboard(request):
    
    if (request.POST):
        user_mail = request.POST.dict()
        mail = user_mail['user_mail']

    url = "http://api.ripe.ai/api/1.0/users/ripe/resetpassword"
    data = "email="+mail
    headers = {
    'clientid': "12121212",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'csrftoken': 'TLUdMBqStZSZNeHUxIYdiwA2cudJaNoTSiIXzPk6T9paLuBIR4T96c1VhKNj4R8l'
    }

    response=requests.request("POST", url, data=data, headers=headers)
    data = response.json()


    if len(data['err']) != 0:
        return HttpResponse("please enter proper registed email :" + data['err']['status'])
    else:
        return redirect('index')
        
        

