#coding:utf-8
from untils.send_request import send_request

def test_send_request():
    url="http://127.0.0.1:9000/articles/"
    headers = {
        "X-Token":"0a6db4e59c7fff2b2b94a297e2e5632e"
    }
    res = send_request("GET",url,headers=headers)
    print(res.json())


if __name__ == "__main__":
    test_send_request()