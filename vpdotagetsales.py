#coding=utf-8

import urllib2
import urllib
import re
import HTMLParser
import csv


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
        with open('heros.csv','wb')as csvfile:
            spamwriter=csv.writer(csvfile,dialect='excel')
            for content in contents:
                #urllib.urlretrieve(content[0],'%s.png'%content[1].decode('utf-8'))
                spamwriter.writerow([content[0],content[1]])

    def getheros(self):
        pattern='(http://thumb.vpgamecdn.com/crop/59.*?.png)" width="59" height="33" alt="(.*?)"'
        pageinfo=self.getpage()
        patt=re.compile(pattern)
        contents=patt.findall(pageinfo)
        heros=[]
        for content in contents:
            heros.append(content[1].decode('utf-8'))
        return heros

    def getheroinfo(self,hero):
        '''
        herourl='http://dota2.vpgame.com/market/default.html?SteamItem[npc]=npc_dota_hero_%s&SteamItem[rarity]=&SteamItem[quality]=&SteamItem[bet]=&SteamItem[zh_name]=&lang=zh_cn'%hero
        request=urllib2.Request(herourl)
        response=urllib2.urlopen(request)
        return response.read().decode('utf-8').encode('gbk')
        '''
        pattern=r'>([0-9]+?)</a></li>\n<li class="next">'
        patt=re.compile(pattern,re.S)
        pageurl='http://dota2.vpgame.com/market/default.html?SteamItem[npc]=npc_dota_hero_%s&SteamItem[rarity]=&SteamItem[quality]=&SteamItem[bet]=&SteamItem[zh_name]=&lang=zh_cn&MarketProduct_page=1'%hero
        request1=urllib2.Request(pageurl)
        pageinfo=urllib2.urlopen(request1).read()
        pages=re.search(patt,pageinfo)
        if pages:
            pages=pages.group(1)
            pages=int(pages)
            #print pages
        else:
            pages=1
        page=1
        responses='a'
        while page<=pages:
            herourl='http://dota2.vpgame.com/market/default.html?SteamItem[npc]=npc_dota_hero_%s&SteamItem[rarity]=&SteamItem[quality]=&SteamItem[bet]=&SteamItem[zh_name]=&lang=zh_cn&MarketProduct_page=%s'%(hero,page)
            page+=1
            '''
            try:
                request=urllib2.Request(herourl)
                response=urllib2.urlopen(request)
                print herourl
                print type(response)
                print type(urllib2.urlopen(request))
                return response.read()
            except urllib2.URLError,e:
                if hasattr(e,'reason'):
                    return None
            '''
            request=urllib2.Request(herourl)
            response=urllib2.urlopen(request).read()
            if response:
                responses+=response
            else:
                pass
        return responses.decode('utf-8').encode('gbk')
            

    def getsale(self,hero):
        pattern=r'<span class="sell-c mr-10">(.*?)</span>(.*?)</p>\n<span class="">(.*?)</span>(.|\n)*?<div class="td">\n<span>(.*?)</span>'
        info=self.getheroinfo(hero)
        patt=re.compile(pattern,re.S)
        contents=re.findall(patt,info)
        return contents
        '''
        if info:
            contents=re.findall(patt,info)
            return contents
        else:
            return None
        '''
    def start(self):
        heros=self.getheros()
        for hero in heros:
            sales=self.getsale(hero)
            filename='%s.csv'%hero
            with open(filename,'wb')as csvfile:
                spamwriter=csv.writer(csvfile,dialect='excel')
                for sale in sales:
                    spamwriter.writerow([sale[0],sale[1],sale[2],sale[4]])
            print 'Finish the sales info for %s'%hero
    
a=site('http://dota2.vpgame.com/market.html')
a.start()
