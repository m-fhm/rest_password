from urllib.parse import urljoin
import requests
import json
import jwt
from dashboard_csr import views

# Create your views here.
from django.http import HttpResponse


def controller_get_jwt_token(token):
    global jwt_token
    jwt_token = token
    print(type(jwt_token))
    global userCode 
    payload = jwt.decode(token, "ertugrul2020", algorithms=["HS256"])
    userCode = payload['userCode']



# def controller_user_password_rest_through_dashboard(email):
def controller_user_password_rest_through_dashboard(mail):
    url = "http://api.ripe.ai/api/1.0/users/ripe/resetpassword"
    data = "email="+mail
    print(data)
    headers = {
    'clientid': "12121212",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }
    response=requests.request("POST", url, data=data, headers=headers).json()
    return response   

# allow to go polls public by csr 
def controller_allow_polls_public(pollid):
    base_url = "http://api.ripe.ai/api/2.0/poll/"
    md_url =  userCode+ "/" +pollid+ "/state/public"
    url = urljoin(base_url,md_url)\
    print(type(jwt_token))

    # print(url) 
    # headers = {
    # 'clientid': "12121212",
    # 'authorization': "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyQ29kZSI6IjBtajAyZGQyIiwiZXhwIjoxNjE5NTM0NTE0NDQ3fQ.0XVmXrIEQ_GPU3RKmnFCW7u1B7TRVSKhKvjNQXIv1cI",
    # 'cache-control': "no-cache",
    # 'postman-token': "c732d64f-51f4-58ff-625c-e7107f9b76f2"
    # }
    headers = {
        'clientid': "1209487",
        }
    response = requests.request("POST", url, headers=headers).json()
    # print(response.json())
    return response

def controller_get_user_survey_questions(surveyid):
    base_url = "http://api.ripe.ai/api/2.0/survey"
    md_url = userCode+"/"+"606c6dc088381136e86703fb"
    url = urljoin(base_url,md_url)
    headers = {
    'clientid': "1209487",
    'authorization': "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyQ29kZSI6IjBtajAyZGQyIiwiZXhwIjoxNjE5NTM0NTE0NDQ3fQ.0XVmXrIEQ_GPU3RKmnFCW7u1B7TRVSKhKvjNQXIv1cI",
    'cache-control': "no-cache",
    'postman-token': "99004a3a-d44c-e601-53bc-8277558eabc4"
    }
    response = requests.request("POST", url, headers=headers)
    response_json = response.json()
    print(response_json)
    # print(response_json)
    # kioskObject = json.loads(response_json['kioskObject'])
    # for n in kioskObject.keys():
    #     print(n)

    
