# -*- coding:utf-8 -*-
'''
Created on 2016年12月6日

@author: huangjiaxin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import multiprocessing
import time
import re
import sys
import pymongo
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


def get_numbers():
    connect = MySQLdb.connect(host="localhost",user="qzone_spider",passwd="qzone_spider",db="db_qzone_spider",charset="utf8")

    cur = connect.cursor()
    cur.execute("select * from t_base_qq")
    cur.scroll(0)
    p = cur.fetchone()
    numbers = []
    try:
        while p:
            numbers.append(str(p[1]))
            p = cur.fetchone()
    finally:
        cur.close()
        connect.close()
    return numbers


def signin(login_number):
    driver = webdriver.PhantomJS()
    url = "http://qzone.qq.com/"
    driver.get(url)
    driver.switch_to_frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(login_number["number"])
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(login_number["password"])
    driver.find_element_by_id('login_button').click()
    time.sleep(7)
    return driver


def dojudge(page_code):
    soup = BeautifulSoup(page_code, 'html.parser')
    if soup.find(name='body', attrs={'class':'no_privilege'}):
        return False
    else:
        return True
    
    
def getcode(driver,QQ_number):
    url = "http://user.qzone.qq.com/" + str(QQ_number)+ "/mood"
    driver.get(url)
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,"app_canvas_frame")))
    driver.switch_to_frame('app_canvas_frame')
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"msgList")))
    time.sleep(15)
    return driver.page_source,driver


def getimformation(page_code):
    soup = BeautifulSoup(page_code, "html.parser")
    temp_imformation = {}
    num = 1
    try:
        for li in soup.find_all(name="li", attrs={"class":"feed"}):
#         print li
    #说说内容
            li_imformation = {}
            shuoshuo_comment = li.find(name="div", attrs={"class":"bd"})
#             print "说说内容",str(shuoshuo_comment.pre)
            li_imformation["shuoshuo"] = str(shuoshuo_comment.pre)
    #转发或者是自发的图片等链接
            picture_or_url = li.find(name="div", attrs={"class":"md"})
#             print "图片或链接",str(picture_or_url)
            li_imformation["picturl_or_url"] = str(picture_or_url)
    #日期，发送平台
            data_platform_str = ''
#         print "发送时间",li.find(name="div", attrs={"class":"info"}).find_all(name="span").string
            for data_platform in li.find(name="div", attrs={"class":"info"}).find_all(name="span"):
                data_platform_str = data_platform_str+'/'+str(data_platform.string)
#             print str(data_platform.string)
            
#             print "data_platform_str:",data_platform_str
            li_imformation["data_platform_str"] = data_platform_str
    #评论和转发人数
            pl_tr = []
#         print li.find(name="div", attrs={"class":"ft"}).find(name="div", attrs={"class":"op"})
            for plnum_trnum in li.find(name="div", attrs={"class":"ft"}).find(name="div", attrs={"class":"op"}).find_all(name="a"):
                pl_tr.append(str(plnum_trnum.string))
#                 print plnum_trnum.string
        
    #点赞列表
            dianzan = li.find(name="div", attrs={"class":"feed_like"})
#             print "ID:",str(dianzan["id"])
            dianzan_ID = str(dianzan["id"])
            li_imformation["dianzan_ID"] = dianzan_ID
    #评论内容
#             print "评论内容"
            pl_content = li.find(name="div", attrs={"class":"comments_list"}).ul
#         print "pl_tr[6]",len(pl_tr[1])
            if len(pl_tr[1]) > 6 or len(pl_tr[6]) >6:
                pl_people_list =[]
                pl_content_list = []
                for pl_item in pl_content.find_all(name="li",attrs={"class":"comments_item bor3"}):
#             print pl_item
                    pl_hf = ''
                    if pl_item.find(name="div", attrs={"class":"mod_comments_sub"}):
#                 print pl_item
                        pl_people = pl_item.find(name="div", attrs={"class":"ui_avatar"})
#                 print pl_people
#                         print "评论人:",re.findall(r'/(\d*)/',str(pl_people.a["href"]))[1]
                        pl_people_number = re.findall(r'/(\d*)/',str(pl_people.a["href"]))[1]
                        if pl_people_number not in pl_people_list:
                            pl_people_list.append(pl_people_number)
                        pl_list = pl_item.find(name="div", attrs={"class":"comments_content"}).find_all("span")
#                     print pl_item.find(name="div", attrs={"class":"comments_content"})
#                     print "LENGTH:",len(pl_list)
                        if len(pl_list) >= 3:
#                             print "评论content:",str(pl_list[2].string),"评论时间",str(pl_list[-2].string)
                            pl_hf = pl_hf +'/'+str(pl_list[2].string)+'/'+str(pl_list[-2].string)
                        else:
#                             print "评论content:",str(pl_list[0].string),"评论时间",str(pl_list[1].string)
                            pl_hf = pl_hf +'/'+str(pl_list[2].string)+'/'+str(pl_list[-2].string)
                        if pl_item.find("ol"):
                            for hf_item in pl_item.find("ol").find_all("li"):
#                         print hf_item
                                hf_people = hf_item.find(name="div", attrs={"class":"ui_avatar"})
#                                 print "回复人:",re.findall(r'/(\d*)/',str(hf_people.a["href"]))[1]
                                hf_people_number = re.findall(r'/(\d*)/',str(hf_people.a["href"]))[1]
                                if hf_people_number not in pl_people_list:
                                    pl_people_list.append(hf_people_number)
                                hf_list = hf_item.find(name="div", attrs={"class":"comments_content"}).find_all("span")
#                                 print "回复content:",str(hf_list[-2].string),"回复时间",str(hf_list[-1].string)
                                pl_hf = pl_hf+'/'+str(hf_list[-2].string)+'/'+str(hf_list[-1].string)
                    pl_content_list.append(pl_hf)
            else:
                pl_people_list =[]
                pl_content_list = []
#                 print "没有人评"  
            li_imformation["pl_people_list"] = pl_people_list
            li_imformation["pl_content_list"] = pl_content_list
            temp_imformation[str(num)] = li_imformation
            num +=1
    except:
        temp_imformation[str(num)] = li_imformation    
    return temp_imformation


def main(signnumber,numbers):
    client = pymongo.MongoClient("localhost",27017)
    database = client.db_shuoshuo_content
    table_imformation = database.t_shuoshuo_mood_content
    table_load = database.t_number_load
    driver = signin(signnumber)
    for number in numbers:
        try:
            page_code,driver = getcode(driver, number)
#     print page_code
            if dojudge(page_code) == True:
                load_dict = {"QQ_number":str(number),"can_load":"1"}
                imformation_dict = getimformation(page_code)
            else:
                load_dict = {"QQ_number":str(number),"can_load":"0"}
                imformation_dict = {}
#             print imformation_dict
        except:
            load_dict = {"QQ_number":str(number),"can_load":"0"}
            imformation_dict = {}
#         print load_dict
#         print imformation_dict
        total_imformation_dict = dict(load_dict, **imformation_dict)
        table_imformation.insert(total_imformation_dict)
        table_load.insert(load_dict)
        time.sleep(3)
    driver.quit()
    client.close()
    

# signnumber = {"number":"", "password":""}
# numbers = ['924785452','281179']
# main(signnumber, numbers)
    
if __name__ == "__main__":
    signnumber = {"number":"", "password":""}
    numbers = get_numbers()
    main(signnumber, numbers)
