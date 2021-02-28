import datetime
import requests

def getToday():
    today = datetime.date.today()
    return today

def login(userid,password):
    payload = {'userid':userid,'password':password}
    # print(payload)
    r = requests.post('https://tokogeko.net/api/login',data=payload)
    # print(r.status_code)
    if r.status_code == 200:
        token = r.headers['Authorization']
    else:
        token = ''
    return token

def getAuth(headers):
    r = requests.get('https://tokogeko.net/api/auth',headers=headers)
    return r