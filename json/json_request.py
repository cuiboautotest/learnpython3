import  json
import  requests

r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=西安')
print(r.json())