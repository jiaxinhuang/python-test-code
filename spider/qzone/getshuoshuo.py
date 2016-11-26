#-*- coding:utf-8 -*-
'''
Created on 2016年11月23日

@author: huangjiaxin
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import sys
# import pymongo
reload(sys)
sys.setdefaultencoding('utf-8')

def load(number):
    driver = webdriver.PhantomJS()
    url = 'http://user.qzone.qq.com/'+str(number)+'/main'
#     print url
    try:
        driver.get(url)
        time.sleep(2)
        if dojudge(driver.page_source, number) != True:
            print number,'can not load'
            driver.quit()
        else:
            driver.switch_to_frame('login_frame')
            driver.find_element_by_id('switcher_plogin').click()
            driver.find_element_by_id('u').clear()
            driver.find_element_by_id('u').send_keys('your_number')
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys('your_passwd')
            driver.find_element_by_id('login_button').click()
            time.sleep(3)
#     print driver.page_source
            if dojudge(driver.page_source, number) == True:
                print number,"can load"
                temp_dict = get_information(driver)
                temp_dict["QQ_number"] = str(number)
                temp_dict["can_load"] = "1"
            else:
                print number,"can not load"
                driver.quit()
                temp_dict = {"QQ_number":str(number), "can_load":"0"}
    except:
        temp_dict = {"QQ_number":str(number), "can_load":"0"}
        print number,'can not load'
        driver.quit()
    return temp_dict


def get_information(driver):
    #click the buttom to content
    driver.find_element_by_id('aOwnerFeeds').click()
    time.sleep(4)
    driver.switch_to_frame('QM_Feeds_Iframe')
    #catch the information that we need
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()
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
        if len(pinglun) > 2:
            print "评论"
            a = 1
            for item in fenli_information.find(name='div', attrs={'class':'comments-list'}).find_all(name='li', attrs={'data-type':'commentroot'}):
            #评论发起人
                item = []
                pinglun_start = item.find(name='div',attrs={'class':'comments-content'})
                print '评论人(qq):',re.findall(r'_(\d*)',str(pinglun_start.a['link']))[0],'内容:',str(pinglun_start.contents[2]),'评论时间:',str(pinglun_start.span.string)
                item.append(re.findall(r'_(\d*)',str(pinglun_start.a['link']))[0]+'+'+str(pinglun_start.contents[2])+'+'+str(pinglun_start.span.string))
            #回复提取
                huifuS = item.find(name='div',attrs={'class':'comments-list mod-comments-sub'}) 
                for huifu in huifuS.find_all('li'):
                    print '回复人（qq）:',str(huifu['data-uin']),'回复内容:',str(huifu.find(name='div',attrs={'class':'comments-content'}).contents[4]),'回复时间:',str(huifu.find(name='div',attrs={'class':'comments-op'}).span.string)
                    item.append(str(huifu['data-uin'])+'+'+str(huifu.find(name='div',attrs={'class':'comments-content'}).contents[4])+'+'+str(huifu.find(name='div',attrs={'class':'comments-op'}).span.string))
                pinglun_dict[str(a)] = item
                a = a+1
        temp_imformation_dict[str(sign_num)] =li_imformation_dict
        sign_num = sign_num+1
    return temp_imformation_dict


def dojudge(content,number):
    soup=BeautifulSoup(content,'lxml')
    if soup.find(name='body', attrs={'class':'no_privilege'}):
        return False
    else:
        return True


def main(numbers):  
#     client = pymongo.Connection("localhost",27017)
#     database = client.db_shuoshuo_content
#     table = database.t_shuoshuo_content
    for number in numbers:    
        try:
            information_dict = load(number)
        except:
            information_dict = {"QQ_number":str(number), "can_load":"0"}
            print number,'can not load'
        print information_dict
#         table.insert(information_dict)
        information_dict = {}
        

numbers = []
main(numbers)