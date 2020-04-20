# -*- coding: utf-8 -*-
from Excelop import Excelop
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


rateYaer={
    '2009':6.8367,
    '2010':6.8281,
    '2011':6.6215,
    '2012':6.3001,
    '2013':6.2897,
    '2014':6.1428,
    '2015':6.2284,
    '2016':6.6423,
    '2017':6.7518,
    '2018':6.6174,
}

def login():
    browser.get("http://data-cnki-net.wvpn.ncu.edu.cn/")
    time.sleep(3)
    if browser.find_element_by_id("user_login"):
        browser.find_element_by_id("user_login").send_keys("410233118353")
    time.sleep(1)
    if browser.find_element_by_id("user_password"):
        browser.find_element_by_id("user_password").send_keys("080925")
    time.sleep(1)
    if browser.find_element_by_name("commit"):
        browser.find_element_by_name("commit").click()
    time.sleep(3)
    browser.get("http://data-cnki-net.wvpn.ncu.edu.cn/")
    time.sleep(3)
    if browser.find_element_by_id("searchKeyword"):
        browser.find_element_by_id("searchKeyword").send_keys(SearchKey)
        browser.find_element_by_id("c_search_btn").click()
    time.sleep(10)
    browser.current_window_handle  # 获取当前窗口
    n = browser.window_handles  # 获取所有窗口
    browser.switch_to_window(n[1])  # 切换到指定窗口




def search(place,Year):
    #browser.implicitly_wait(15)
    if browser.find_element_by_name("IndicateRegion"):
        browser.find_element_by_name("IndicateRegion").clear()
        browser.find_element_by_name("IndicateRegion").send_keys(place)

    time.sleep(1)
    select = Select(browser.find_element_by_id("StartYear"))
    select.select_by_visible_text(Year)
    time.sleep(1)
    select2 = Select(browser.find_element_by_id("EndYear"))
    select2.select_by_visible_text(Year)
    time.sleep(3)
    if browser.find_element_by_id("AdvancedSearch"):
        browser.find_element_by_id("AdvancedSearch").click()
    time.sleep(2)
    data =Find_key()
    return data


def Find_key():
    #td[6]是要的数值  td[5]是关键字名称
    # 获取table的行数
    while(1):
        time.sleep(1)
        data = 0.0
        rowCount = len(browser.find_elements_by_xpath('//*[@id="t1"]/tbody/tr'))
        # 获取第三列的每一行的值
        for i in range(1, rowCount+1):
            if browser.find_element_by_xpath('//*[@id="t1"]/tbody/tr[%s]/td[5]' % (i)).text == SearchKey:
                print("找到目标")
                data = float(browser.find_element_by_xpath('//*[@id="t1"]/tbody/tr[%s]/td[6]'% (i)).text)
                if browser.find_element_by_xpath('//*[@id="t1"]/tbody/tr[%s]/td[7]' % (i)).text == "万美元":
                    data = data / 10000.0
                break
        if data==0.0:
            if rowCount < 10:
                break
            if browser.find_element_by_id("NextPage"):
                browser.find_element_by_id("NextPage").click()
        else:
            break
    print(data)
    return data

def Rate_Year():
    print("set rate of excel")
    i=0
    for Year in range(2009,2019):
        rate=rateYaer.get(str(Year))
        for key in d:
            data=float(mExcel.read(int(d.get(key))+i,14))*rate
            mExcel.Write_data_save(int(d.get(key))+i,16,str(data))
        i=i+1


def Get_data():
    print("get data from net")
    login()
    i=0
    for Year in range(2009,2019):
        for key in d:
            data=float(search(key,str(Year)))
            mExcel.Write_data_save(int(d.get(key))+i,12,str(data))
        i=i+1




if __name__ == '__main__':
    SearchKey="外商直接投资额"
    #init webdriver
    #@browser = webdriver.Chrome()

    #init escel
    mExcel=Excelop(r'C:\Users\18136\Desktop\11.xlsx',"2009-2018",0)
    d= mExcel.Get_dict()

    #run
    #Get_data()
    Rate_Year()
