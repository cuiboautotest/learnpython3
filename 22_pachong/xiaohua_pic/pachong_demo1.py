import requests
from lxml import etree
startUrl='http://www.xiaohuar.com/list-1-'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}
for i in range(10):
    url=requests.get(startUrl+str(i)+'.html',headers=headers).content.decode('gbk')
    story=etree.HTML(url)
    photo_name=story.xpath('//div[@class="img"]')
    try:
        for i in photo_name:
            name=i.xpath('./a/img/@alt')[0]
            photo=i.xpath('./a/img/@src')[0]
            photo='http://www.xiaohuar.com'+str(photo)
            img = requests.get(photo,headers=headers,stream=True).content
            with open('img/'+str(name)+'.jpg','wb') as f:
                f.write(img)
            print("正在下载：",name)
    except:
        print('当前页面所有美眉图片下载完毕！')
