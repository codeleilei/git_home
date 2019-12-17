#-*- coding: UTF-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time


def login(uname, pwd):
  # 打开淘宝登录页，并进行扫码登录
  browser.get("https://www.taobao.com")
  time.sleep(3)
  if browser.find_element_by_link_text("亲，请登录"):
      browser.find_element_by_link_text("亲，请登录").click()
  time.sleep(1)
  if browser.find_element_by_link_text("密码登录"):
    browser.find_element_by_link_text("密码登录").click();
  time.sleep(1)
  if browser.find_element_by_name("TPL_username"):
      browser.find_element_by_name("TPL_username").send_keys(uname);
  time.sleep(1)
  if browser.find_element_by_name("TPL_password"):
      browser.find_element_by_name("TPL_password").send_keys(pwd);
  time.sleep(2)
  if browser.find_element_by_id("J_SubmitStatic"):
      browser.find_element_by_id("J_SubmitStatic").click();
  time.sleep(15)
  browser.get("https://cart.taobao.com/cart.htm")
  time.sleep(1)
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times, choose):
  if choose == 1:
    while True:
      try:
        if browser.find_element_by_id("J_SelectAll2"):
          browser.find_element_by_id("J_SelectAll2").click()
          break
      except:
        print("找不到购买按钮")
  else:
    print("请手动勾选需要购买的商品")
  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    if now >= times:
      # 点击结算按钮
      while True:
        try:
          if browser.find_element_by_link_text("结 算"):
            browser.find_element_by_link_text("结 算").click()
            print("结算成功")
            break
        except:
          pass
      while True:
        try:
          if browser.find_element_by_link_text('提交订单'):
            browser.find_element_by_link_text('提交订单').click()
            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print("抢购成功时间：%s" % now1)
        except:
          print("再次尝试提交订单")
      time.sleep(0.0001)


#中文账号的时候要给它编码一下，不然会出错
#login("中文账号".decode('utf-8'),'密码')
if __name__ == "__main__":
    times = '2019-12-17 11:01:00.000'
    # 时间格式："2018-09-06 11:20:00.000000"
#不加载图片和javascript    要加载javascript 不然找不到按钮
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
           # 'images': 2
            #'javascript': 2
        }
    }
    options.add_experimental_option('prefs', prefs)

#end
#使用headless  这个在linux无gui的情况下运行
    #options.headless = True # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
#使用手机版phone  ---一般这种的反爬技术比较落后
    #options.add_argument('user-agent={0}'.format(
               # 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'))

# 开发者模式的开关，设置一下，打开浏览器就不会识别为自动化测试工具了
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = webdriver.Chrome(chrome_options=options)

    browser.maximize_window()
    login("a1813612013", 'zilu0130')
    choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(times,choose)