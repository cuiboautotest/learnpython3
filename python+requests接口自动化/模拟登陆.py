#coding=utf-8
import requests
# 禅道host地址
host = "https://10.91.3.74"

def login(s,username,password,authcode):
    url = host+"/skyeye/admin/login"
    print(url)
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Referer": host+"/",
        # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        }

    body1 = {"username": username,
             "password": password,
             "authcode": authcode
            }

    # s = requests.session()   不要写死session
    r1 = s.post(url, data=body1, headers=h)
    # return r1.content  # python2的return这个
    return r1.content.decode("utf-8")  # python3

def is_login_sucess(res):
        if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
                return False
        elif "parent.location=" in res:
                return True
        else:
                return False

if __name__ == "__main__":
    s = requests.session()
    a = login(s, "sysadmin", "admin321","e5jm")
    result = is_login_sucess(a)
    print("测试结果：%s"%result)