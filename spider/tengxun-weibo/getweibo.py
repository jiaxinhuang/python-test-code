# -*- coding:utf-8 -*-
'''
Created on 2016年12月13日

@author: huangjiaxin
'''

import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getpage(user_id):
    url = "http://t.qq.com/" + str(user_id)
    r = requests.get(url)
    return r.text


def getimformation(page_code):
    soup = BeautifulSoup(page_code,'html.parser')

    private_information = soup.find(name="div", attrs={"id":"LUI_wide"})
# print private_information
    user_name = private_information.find(name="h3").a
    print "用户名：",user_name.string
    user_level = private_information.find(name="h3").find(name="a", attrs={"class":"ico_level"}).em
    print "level:",user_level.string

    detail_information = private_information.find(name="div", attrs={"class":"m_profile_info"})
    city = detail_information.find(name="p", attrs={"class":"desc"}).find(name="a", attrs={"boss":"btnApolloCity"})
    if city:
        print "the city:",city.string
    else:
        print "the city is None"
    work = detail_information.find(name="p", attrs={"class":"desc"}).find(name="a", attrs={"boss":"btnApolloWork"})
    if work:
        print "the work:",work.string
    else:
        print "the work is None"

    summary = detail_information.find(name="p", attrs={"class":"summary"})
    print "the summary:",summary

    follow_information = private_information.find(name="div", attrs={"class":"m_profile"})
    messageCount = follow_information.find(name="a", attrs={"boss":"btnApolloMessageCount"}).span
    print "the num of messageCount:",messageCount.string
    fllowingCount = follow_information.find(name="a", attrs={"boss":"btnApolloFollowing"}).span
    print "the num of following:",fllowingCount.string
    followerCount = follow_information.find(name="a", attrs={"boss":"btnApolloFollower"}).span
    print "the num of follower:",followerCount.string

    for item in soup.find(name="ul", attrs={"id":"talkList"}).find_all(name="li"):
#     print item
        msg_content = item.find(name="div", attrs={"class":"msgCnt"})
        print "msg_content:",msg_content
    
        tran_content = item.find(name="div", attrs={"class":"replyBox"})
        print "tran_content:",tran_content
        picturl_or_vedio = item.find(name="div", attrs={"class":"clear"})
        print "picturl_or_vedio:",picturl_or_vedio
    
        public_information = item.find(name="div", attrs={"class":"pubInfo"})
        platform = public_information.find(name="i", attrs={"class":"sico"})
        if platform:
            print "platform:",platform["title"]
        else:
            print "platform is None"
        date_time = public_information.find(name="a", attrs={"class":"time"})
        print "date_time:",date_time.string
        

def main(user_id):
    page_code = getpage(user_id)
    getimformation(page_code)
    

if __name__ == "__main__":          
    user_id = ['tongchunfeng1', 'huwang-ranmeng', 'szftpea', 'chenbingyu3068', 'sz3yecao','zhaijing84','zhuyinnian', 'gonghaiyan', 'hexintoys', 'yi_shu']
    main(user_id[5])