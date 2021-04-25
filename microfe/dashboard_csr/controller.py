from urllib.parse import urljoin
import requests
import json
import jwt

# Create your views here.
from django.http import HttpResponse


def controller_get_jwt_token(request):
    global userCode
    token = request.GET.get('token')
    payload = jwt.decode(token, "ertugrul2020", algorithms=["HS256"])
    userCode = payload['userCode']

def controller_index(request):
    title = 'Reports'
    code = 'X3'
    info1 = request.GET
    info2 = request.POST
    info3 = request.COOKIES
    info4 = request.META
    info5 = request.FILES
    info6 = request.path
    method = request.method
    return code,title
    # # html = render_to_string('dashboard_csr.html', {'method': method, 'title': title, 'code': code, 'info1': info1, 'info2': info2, 'info3': info3, 'info4': info4, 'info5': info5, 'info6': info6})
    # html = render_to_string('dashboard_csr.html',{'code':code, 'title': title})
    # return HttpResponse(html)

def controller_user_password_rest_through_dashboard(request):
    if (request.POST):
        user_mail = request.POST.dict()
        mail = user_mail['user_mail']

    url = "http://api.ripe.ai/api/1.0/users/ripe/resetpassword"
    data = "email="+mail
    headers = {
    'clientid': "12121212",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }

    response=requests.request("POST", url, data=data, headers=headers)
    data = response.json()
    return data    

# allow to go polls public by csr 
def controller_allow_polls_public(request):

    if (request.POST):
        user_mail = request.POST.dict()
        pollid = user_mail['pollid']

    base_url = "http://api.ripe.ai/api/2.0/poll/"
    md_url =  userCode+ "/" +pollid+ "/state/public"
    url = urljoin(base_url,md_url)
    print(url) 
    headers = {
        'clientid': "1209487",
        }

    response = requests.request("POST", url, headers=headers)
    # print(response.json())
    return response

def controller_get_user_survey_questions(request):
    if (request.POST):
        user_mail = request.POST.dict()
        surveyid = user_mail['surveyid']

    base_url = "http://api.ripe.ai/api/2.0/survey/"
    md_url = userCode+"/"+surveyid
    url = urljoin(base_url,md_url)
    headers = {
        'clientid': "1209487",
        }
    response = requests.request("POST", url, headers=headers)
    response_json = response.json()
    # print(response_json)
    kioskObject = json.loads(response_json['kioskObject'])
    # for n in kioskObject.keys():
    #     print(n)
    return kioskObject
    