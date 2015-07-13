# !coding=utf-8

import urllib2
import urllib
import re
import HTMLParser

class site():
    def __init__(self,inputurl):
        self.inputurl=inputurl
        
    def getpage(self):
        request=urllib2.Request(self.inputurl)
        getpage=urllib2.urlopen(request)
        pageinfo=getpage.read().decode('utf-8')
        return pageinfo

    def getpic(self):
        pattern='(http://thumb.vpgamecdn.com/crop/59.*?.png)" width="59" height="33" alt="(.*?)"'
        pageinfo=self.getpage()
        patt=re.compile(pattern)
        contents=patt.findall(pageinfo)
        print contents
        for content in contents:
            urllib.urlretrieve(content[0],'%s.png'%content[1].decode('utf-8'))
    
a=site('http://dota2.vpgame.com/market.html')
a.getpic()
