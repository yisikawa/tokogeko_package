
import json
from tokogeko_package import utils

token =''

def main():
    # get token & set headers
    global token
    token = utils.login('test','test123')
    headers = {'Authorization': '{}'.format(token)}
    print(headers)
    # get today
    today = utils.getToday()
    print(today)
    #get auther
    r = utils.getAuth(headers)
    users = json.loads(r.text)
    # for user in users:
    #     print(user)
    # 地図オブジェクト作成

if __name__ == '__main__':
    main()
