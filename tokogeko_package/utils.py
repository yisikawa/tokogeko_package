import datetime
import requests

def getToday():
    today = datetime.date.today()
    return today
# login tokenを取得
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
# 参照userリストを取得
def getAuth(headers):
    r = requests.get('https://tokogeko.net/api/auth',headers=headers)
    return r
# 登下校経路を取得
def getPersonalPath(headers,userID,date,type):
    str = 'https://tokogeko.net/api/route?'+f'userid={userID}'+f'&date={date}'+f'&type={type}'
    r = requests.get(str,headers=headers)
    return r.text