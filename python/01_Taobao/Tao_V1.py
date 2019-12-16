# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/03/16
# 淘宝秒杀脚本，扫码登录版   V4----------1.75秒
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import datetime
import random
import time


def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times,choose):
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


if __name__ == "__main__":
    times = '2019-12-17 00:44:00.000'
    # 时间格式："2018-09-06 11:20:00.000000"
#不加载图片和javascript    要加载javascript 不然找不到按钮
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
            #'javascript': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
#end

    browser = webdriver.Chrome(chrome_options=options)
    browser.maximize_window()
    login()
    choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(times,choose)