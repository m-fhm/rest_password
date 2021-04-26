#standards libs
from django.shortcuts import render,redirect
# from django.template.loader import render_to_string
from django.http import HttpResponse

#custom imports from controller.py
from dashboard_csr import controller


def get_jwt_token(request):
    global token
    token = request.GET.get('token')
    
    controller.controller_get_jwt_token(token)
    return redirect('index')

def index(request):
    title = 'Reports'
    code = 'X3'
    info1 = request.GET
    info2 = request.POST
    info3 = request.COOKIES
    info4 = request.META
    info5 = request.FILES
    info6 = request.path
    method = request.method
    # # html = render_to_string('dashboard_csr.html', {'method': method, 'title': title, 'code': code, 'info1': info1, 'info2': info2, 'info3': info3, 'info4': info4, 'info5': info5, 'info6': info6})
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    # return HttpResponse(html)
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    return render(request,'dashboard_csr.html',{'code':code, 'title': title})

def user_password_rest_through_dashboard(request):
    if (request.POST):
        user_mail = request.POST.dict()
        mail = user_mail['user_mail']
    data = controller.controller_user_password_rest_through_dashboard(mail)

    if len(data['err']) != 0:
        return HttpResponse("please enter proper registed email :" + data['err']['status'])
    else:
        return redirect('index')
    
# allow to go polls public by csr 
def allow_polls_public(request):
    if (request.POST):
        user_mail = request.POST.dict()
        pollid = user_mail['pollid']
    response = controller.controller_allow_polls_public(pollid)
    return redirect('index')

def get_user_survey_questions(request):
    if (request.POST):
        form_post = request.POST.dict()
        surveyid = form_post['surveyid']
    kioskObject=controller.controller_get_user_survey_questions(surveyid)
    # appid = kioskObject['appId']
    # screentitle= kioskObject['screen_title']
    return render(request,'dashboard_csr.html')
    
