# -*- coding:utf-8 -*-
'''
Created on 2016年11月29日

@author: huangjiaxin
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import multiprocessing
import time
import re
import sys
import pymongo
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

def load(number):
    driver = webdriver.PhantomJS()
    url = 'http://user.qzone.qq.com/'+str(number)+'/profile'
    
    try:
        driver.get(url)
        time.sleep(3)
        if dojudge(driver.page_source) !=True:
            dict_load = {"QQ_number":str(number), "can_load":"0"}
            dict_information = {}
            dict_total_information = dict(dict_load, **dict_information)
            driver.quit()
            return dict_load,dict_total_information
        else:
            driver,sign_page_code = getsignpagecode(driver)
    except:
        dict_load = {"QQ_number":str(number), "can_load":"0"}
        dict_information = {}
        dict_total_information = dict(dict_load, **dict_information)
        driver.quit()
        return dict_load,dict_total_information
    
    if dojudge(sign_page_code) == False:
        dict_load = {"QQ_number":str(number), "can_load":"0"}
        dict_information = {}
        dict_total_information = dict(dict_load, **dict_information)
        driver.quit()
    else:
        dict_load = {"QQ_number":str(number), "can_load":"1"}
        dict_information = {}
        try:
            page_code = getcode(driver)
            dict_information = getinformation(page_code)
        except:
            page_code = getcode(driver)
            dict_information = getinformation(page_code)
        finally:
            dict_total_information = dict(dict_load, **dict_information)
            driver.quit()
    return dict_load,dict_total_information
    

def dojudge(page_code):
    soup = BeautifulSoup(page_code, 'lxml')
    if soup.find(name='body', attrs={'class':'no_privilege'}):
        return False
    else:
        return True

  
def getcode(driver):
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"app_canvas_frame")))
    driver.switch_to_frame('app_canvas_frame')
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"feed_container")))
    driver.switch_to_frame('frameFeedList')
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,"host_home_feeds")))
    return driver.page_source


def getsignpagecode(driver):
    driver.switch_to_frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys('your_number')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('your_password')
    driver.find_element_by_id('login_button').click()
    time.sleep(3)
    return driver,driver.page_source
    

def getinformation(page_code):  
    soup = BeautifulSoup(page_code,'lxml')
    temp_imformation_dict = {}
    sign_num = 1
    for li in soup.find_all(name='li', attrs={'class':'f-single'}):
        li_imformation_dict = {}
        print '发送时间:',str(li.span.string)
        li_imformation_dict["send_time"] = str(li.span.string)
        
        phone_type = li.find(name='a', attrs={'class':'phone-style'})
        if phone_type:
            print '发送平台：',str(li.find(name='a', attrs={'class':'phone-style'}).string)
            li_imformation_dict["send_platform"] = str(li.find(name='a', attrs={'class':'phone-style'}).string)
        else:
            print "发送平台：电脑"
            li_imformation_dict["send_platform"] = "电脑"
            
        print '浏览数: ',re.findall(r'\((\d*)\)',str(li.find(name='a',attrs={'data-clicklog':'visitor'}).contents[1]))[0]
        li_imformation_dict["see_num"] = re.findall(r'\((\d*)\)',str(li.find(name='a',attrs={'data-clicklog':'visitor'}).contents[1]))[0]
        
        shuoshuo_or_comment = li.find(name='div',attrs={'class':'f-info'})
        print str(shuoshuo_or_comment)
        li_imformation_dict["shuoshuo_or_comment"] = str(shuoshuo_or_comment)
        picture_or_url = li.find(name='div',attrs={'class':'f-ct'})
        print str(picture_or_url)
        li_imformation_dict["picture_or_url"] = str(picture_or_url)
        
        #分离评论以及评论人数，转发人数，点赞人数
        fenli_information = li.find(name='div', attrs={'class':'f-op-wrap'})
    
    #评论人数
        pinglun = fenli_information.find(name='a',attrs={'data-clicklog':'comment'}).contents[1]
        if len(pinglun) > 2:
            print '评论人数:',re.findall(r'\((\d*)\)',str(pinglun))[0]
            li_imformation_dict["comment_num"] = re.findall(r'\((\d*)\)',str(pinglun))[0]
        else:
            print '评论人数:',str(0)
            li_imformation_dict["comment_num"] = "0"
    
    #转发人数
        zhuanfa = fenli_information.find(name='a',attrs={'data-clicklog':'retweet'}).contents[1]
        if len(zhuanfa) > 2:
            print '转发人数：',re.findall(r'\((\d*)\)',str(zhuanfa))[0]
            li_imformation_dict["tran_num"] = re.findall(r'\((\d*)\)',str(zhuanfa))[0]
        else:
            print '转发人数：',str(0)
            li_imformation_dict["tran_num"] = "0"
    
    #点赞人数
        dianzan = fenli_information.find(name='a',attrs={'data-clicklog':'like'}).contents[1]
        if len(dianzan) > 1:
            print '点赞人数:',re.findall(r'\((\d*)\)',str(dianzan))[0]
            li_imformation_dict["prise_num"] = re.findall(r'\((\d*)\)',str(dianzan))[0]
        else:
            print '点赞人数:',str(0)
            li_imformation_dict["prise_num"] = "0"
    
    #点赞人列表，转发的点赞是没有显示的
        dianzan_list = fenli_information.find(name='div',attrs={'class':'f-like'})
        prise_list = []
        if dianzan_list != None:
            for user in dianzan_list.find_all(name='a',attrs={'class':'item'}):
                print "空间链接",re.findall(r'/(\d*)',str(user["href"]))[2]
                prise_list.append(re.findall(r'/(\d*)',str(user["href"]))[2])
        else:
            print "can not get the list because of transponding"
        li_imformation_dict["parise_list"] = prise_list
    #评论人列表
        pinglun_dict = {}
        pinglun_people = []
        if len(pinglun) > 2:
            print "评论"
            a = 1
            for item_pinglun in fenli_information.find(name='div', attrs={'class':'comments-list'}).find_all(name='li', attrs={'data-type':'commentroot'}):
            #评论发起人
                item_list = []
                pinglun_start = item_pinglun.find(name='div',attrs={'class':'comments-content'})
                pinglun_people.append(re.findall(r'_(\d*)',str(pinglun_start.a['link']))[0])
                print '评论人(qq):',re.findall(r'_(\d*)',str(pinglun_start.a['link']))[0],'内容:',str(pinglun_start.contents[2]),'评论时间:',str(pinglun_start.span.string)
                item_list.append(re.findall(r'_(\d*)',str(pinglun_start.a['link']))[0]+'+'+str(pinglun_start.contents[2])+'+'+str(pinglun_start.span.string))
            #回复提取
                huifuS = item_pinglun.find(name='div',attrs={'class':'comments-list mod-comments-sub'}) 
                for huifu in huifuS.find_all('li'):
                    print '回复人（qq）:',str(huifu['data-uin']),'回复内容:',str(huifu.find(name='div',attrs={'class':'comments-content'}).contents[4]),'回复时间:',str(huifu.find(name='div',attrs={'class':'comments-op'}).span.string)
                    item_list.append(str(huifu['data-uin'])+'+'+str(huifu.find(name='div',attrs={'class':'comments-content'}).contents[4])+'+'+str(huifu.find(name='div',attrs={'class':'comments-op'}).span.string))
                pinglun_dict[str(a)] = item_list
                a = a+1
#                 print "item_list:",item_list
        print pinglun_people
        li_imformation_dict["pinglun_people_list"] = pinglun_people
        li_imformation_dict["pinglun_list"] = pinglun_dict
        temp_imformation_dict[str(sign_num)] =li_imformation_dict
        sign_num = sign_num+1
    return temp_imformation_dict

    
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


def main(numbers):
    client = pymongo.MongoClient("localhost",27017)
    database = client.db_shuoshuo_content
    table_information = database.t_shuoshuo_content
    table_load = database.t_number_load
    for number in numbers:
        try:
            dict_load,dict_total_information = load(number)
        except:
            dict_load = {"QQ_number":str(number), "can_load":"0"}
            dict_total_information = {"QQ_number":str(number), "can_load":"0"}
#         print dict_load
#         print dict_total_information
        table_information.insert(dict_total_information)
        table_load.insert(dict_load)
        dict_load = {}
        dict_total_information = {}
    client.close()

# numbers = ['1075301448','1677881573','113008722','312315891','2722054136','26002109','1264565466']
# main(numbers)

if __name__ == "__main__":
#     numbers = ['1075301448','1677881573','113008722','312315891','2722054136','26002109','1264565466']
    numbers = get_numbers()
    len_numbers = len(numbers)
    p1 = multiprocessing.Process(target=main, args=(numbers[0:len_numbers/3],))
    p2 = multiprocessing.Process(target=main, args=(numbers[len_numbers/3:len_numbers/3*2],))
    p3 = multiprocessing.Process(target=main, args=(numbers[len_numbers/3*2:],))
    
    p1.start()
    p2.start()
    p3.start()
    
    