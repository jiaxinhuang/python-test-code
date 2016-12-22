# -*- coding:utf-8 -*-
'''
Created on 2016年12月13日

@author: huangjiaxin
'''

import requests
import time
from bs4 import BeautifulSoup
from pybloom import BloomFilter, ScalableBloomFilter
import re
import pymongo
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_users():
    connect = MySQLdb.connect(host="localhost",user="qzone_spider",passwd="qzone_spider",db="db_tencent_wb",charset="utf8")
    cur = connect.cursor()
    cur.execute("select * from t_tencent_wb_wid")
    cur.scroll(0)
    p = cur.fetchone()
    users = []
    try:
        while p:
            users.append(str(p[2]))
            p = cur.fetchone()
    finally:
        cur.close()
        connect.close()
    return users


def getpage(user_id):
    url = "http://t.qq.com/" + str(user_id)
    r = requests.get(url)
    return r.text


def getinformation(page_code):
    information_dict = {}
    soup = BeautifulSoup(page_code,'html.parser')
    try:
        private_information = soup.find(name="div", attrs={"id":"LUI_wide"})
# print private_information
        user_name = private_information.find(name="h3").a
#     print "用户名：",str(user_name.string)
        information_dict["user_name"] = str(user_name.string)
        user_level = private_information.find(name="h3").find(name="a", attrs={"class":"ico_level"}).em
#     print "level:",str(user_level.string)
        information_dict["level"] = str(user_level.string)

        detail_information = private_information.find(name="div", attrs={"class":"m_profile_info"})
        city = detail_information.find(name="p", attrs={"class":"desc"}).find(name="a", attrs={"boss":"btnApolloCity"})
        if city:
#         print "the city:",str(city.string)
            information_dict["city"] = str(city.string)
        else:
            information_dict["city"] = "None"
#         print "the city is None"
        work = detail_information.find(name="p", attrs={"class":"desc"}).find(name="a", attrs={"boss":"btnApolloWork"})
        if work:
#         print "the work:",str(work.string)
            information_dict["user_work"] = str(work.string)
        else:
            information_dict["user_work"] = "None"
#         print "the work is None"

        summary = detail_information.find(name="p", attrs={"class":"summary"})
#     print "the summary:",str(summary)
        information_dict["summary"] = str(summary)

        follow_information = private_information.find(name="div", attrs={"class":"m_profile"})
        messageCount = follow_information.find(name="a", attrs={"boss":"btnApolloMessageCount"}).span
#     print "the num of messageCount:",str(messageCount.string)
        information_dict["messageCount"] = str(messageCount.string)
        fllowingCount = follow_information.find(name="a", attrs={"boss":"btnApolloFollowing"}).span
#     print "the num of following:",str(fllowingCount.string)
        information_dict["following"] = str(fllowingCount.string)
        followerCount = follow_information.find(name="a", attrs={"boss":"btnApolloFollower"}).span
#     print "the num of follower:",str(followerCount.string)
        information_dict["follower"] = str(followerCount.string)

        item_num = 1
        talkList_dict = {}
        for item in soup.find(name="ul", attrs={"id":"talkList"}).find_all(name="li"):
#     print item
            content_dict = {}
            msg_content = item.find(name="div", attrs={"class":"msgCnt"})
#         print "msg_content:",str(msg_content)
            if msg_content != None:
                msg_string = []
                for string in msg_content.stripped_strings:
                    msg_string.append(str(string)) 
#                 print "msg_string:",msg_string
            else:
                msg_string = "None"
            content_dict["msg_content"] = str(msg_string)
    
            tran_content = item.find(name="div", attrs={"class":"replyBox"})
#         print "tran_content:",str(tran_content)
            if tran_content != None:
                tran_string = []
                for string in tran_content.stripped_strings:
                    tran_string.append(str(string))
#                 print "tran_string:",tran_string
            else:
                tran_string = "None"
            content_dict["tran_content"] = str(tran_string)
            
            picturl_or_vedio = item.find(name="div", attrs={"class":"clear"})
#         print "picturl_or_vedio:",str(picturl_or_vedio)
            if picturl_or_vedio != None:
                picturl_or_vedio_string = []
                for string in picturl_or_vedio.stripped_strings:
                    picturl_or_vedio_string.append(str(string)) 
#                 print "picturl_or_vedio_string:",picturl_or_vedio_string
            else:
                picturl_or_vedio_string = "None"
            content_dict["picturl_or_vedio"] = str(picturl_or_vedio_string)
    
            public_information = item.find(name="div", attrs={"class":"pubInfo"})
            platform = public_information.find(name="i", attrs={"class":"sico"})
            if platform:
#             print "platform:",str(platform["title"])
                content_dict["platform"] = str(platform["title"])
            else:
                content_dict["platform"] = "None"
#             print "platform is None"
            date_time = public_information.find(name="a", attrs={"class":"time"})
#         print "date_time:",str(date_time.string)
            content_dict["date_time"] = str(date_time.string)
            talkList_dict[str(item_num)] = content_dict
            item_num += 1
        information_dict["talkList"] = talkList_dict
    except:
        return information_dict
    return information_dict
        

def main(user_ids):
    client = pymongo.MongoClient("localhost",27017)
    database = client.db_tx_wb_content
    table_information = database.t_weibo_content
    user_bf = BloomFilter(capacity=100000000, error_rate=0.01)
    for user_id in user_ids:
        if (user_id in user_bf) == False:
            try:
                page_code = getpage(user_id)
                information_dict = getinformation(page_code)
            except:
                information_dict = {"information":"None"}
            information_dict["UserId"] = user_id
#             print information_dict
#             time.sleep(3)
            table_information.insert(information_dict)
#         print information_dict
    client.close()
    

if __name__ == "__main__":          
#     user_ids = ['tongchunfeng1', 'huwang-ranmeng', 'szftpea', 'chenbingyu3068', 'sz3yecao','zhaijing84','zhuyinnian', 'gonghaiyan', 'hexintoys', 'yi_shu']
    user_ids = get_users()
    main(user_ids)
