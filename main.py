from flask import Flask
import folium
import json
from tokogeko_package import utils

app = Flask(__name__)
token =''

@app.route('/')
def hello_world():
    map = folium.Map(location=[35.000081, 137.004055],height=300, zoom_start=15)
    return map

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
    app.debug = True
    app.run()
