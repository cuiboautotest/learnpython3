from selenium import webdriver
import time
from selenium import webdriver
from PIL import Image
import time
import tesserocr

driver=webdriver.Chrome()
def get_snap(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    img = driver.find_element_by_xpath('//*[@id="app-comp"]/div/div[4]/div[2]/div[3]/img')
    time.sleep(2)
    location = img.location
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    # image_obj.show()
    return image_obj  # 得到的就是验证码


def start():
    driver = webdriver.Chrome()
    driver.get('https://10.91.3.13')
    driver.maximize_window()
    # 当爬取zhipin.com 出现验证码时，进入任何一个公司首页都需要验证码，这里拿的是要进入网易的公司首页时显示的验证链接
    # wait = WebDriverWait(driver, 10)
    time.sleep(3)

    image1 = get_image(driver)
    image1.show()  # 可以开启这行，查看所截取的验证码图片是否正确

if __name__ == '__main__':
    start()



