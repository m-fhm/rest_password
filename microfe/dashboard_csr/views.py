#standards libs
from django.shortcuts import render,redirect
# from django.template.loader import render_to_string
from django.http import HttpResponse

#custom imports from controller.py
from dashboard_csr import controller


def get_jwt_token(request):
    controller.controller_get_jwt_token(request)
    return redirect('index')

def index(request):
    code,title=controller.controller_index(request)
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    return render(request,'dashboard_csr.html',{'code':code, 'title': title})

def user_password_rest_through_dashboard(request):
    data = controller.controller_user_password_rest_through_dashboard(request)

    if len(data['err']) != 0:
        return HttpResponse("please enter proper registed email :" + data['err']['status'])
    else:
        return redirect('index')
    
# allow to go polls public by csr 
def allow_polls_public(request):
    response = controller.controller_allow_polls_public(request)
    return redirect('index')

def get_user_survey_questions(request):
    kioskObject=controller.controller_get_user_survey_questions(request)
    appid = kioskObject['appId']
    screentitle= kioskObject['screen_title']
    return render(request,'dashboard_csr.html',{'appid':appid,'screentitle':screentitle})
    
