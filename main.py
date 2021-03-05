import gpxpy
import json
from pytz import timezone
from tokogeko_package import utils

token =''

def main():
    # タイムゾーン
    dt_tz = timezone('Asia/Tokyo')
    # 日時文字列形式
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    # 配列の初期化
    DateTime = []
    Lat = []
    Lng = []
    Alt = []
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
    # 経路取得
    r = utils.getPersonalPath(headers,'geko31c','20200217','1')
    gpx = gpxpy.parse(r)
    for track in gpx.tracks:
        for segment in track.segments:
            points = segment.points
            N=len(points)
            for i in range(N):
                point = points[i]
                datetime = point.time.astimezone(dt_tz).strftime(dt_fmt)
                lat      = point.latitude
                lng      = point.longitude
                alt      = point.elevation
                # データ代入
                DateTime.append(datetime)
                Lat.append(lat)
                Lng.append(lng)
                Alt.append(alt)
                print(f'Datetime={datetime} Lat = {lat} Lng = {lng}')


if __name__ == '__main__':
    main()
