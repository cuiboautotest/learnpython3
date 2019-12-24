cookies = "anonymid=jy0ui55o-u6f6zd; depovince=GW; _r01_=1; JSESSIONID=abcMktGLRGjLtdhBk7OVw; ick_login=a9b557b8-8138-4e9d-8601-de7b2a633f80; _ga=GA1.2.1307141854.1562980962; _gid=GA1.2.201589596.1562980962; _c1=-100; first_login_flag=1; ln_uact=18323008898; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=88f1340c-592c-4dd6-a738-128a76559f45%7Cad33b3c730fcdc8df220648f0893e840%7C1562981108370%7C1%7C1562981106763; jebe_key=88f1340c-592c-4dd6-a738-128a76559f45%7Cad33b3c730fcdc8df220648f0893e840%7C1562981108370%7C1%7C1562981106765; jebecookies=793eb32e-92c6-470d-b9d0-5f924c335d30|||||; _de=E77807CE44886E0134ABF27E72CFD74F; p=a00d65b1f779614cd242dc719e24c73e0; t=292ba8729a4151c1a357e176d8d91bff0; societyguester=292ba8729a4151c1a357e176d8d91bff0; id=969937120; xnsid=1700b2cc; ver=7.0; loginfrom=null; wp_fold=0"
# 字典推导式
cookies = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookies.split("; ")}
print(cookies)

'''
代码分析：

在字符串cookies中’=’前面是key，’=’后面是value，每一个’;’构成一个键值对；多个键值对构成一个字典；

1.根据’;’将字符串拆分为列表；

2.根据第一步获取的列表，遍历时将每一个字符串根据’=’再次拆分；

3.根据第二步拆分的结果，列表第一个元素作为key,列表第二个元素作为value；
'''