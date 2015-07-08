#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import re

class Tool:
    removeTitle=re.compile(r'<title>|</title>')
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    replaceTD=re.compile('<td>')
    def replace(self,x):
        x=re.sub(self.removeTitle,"",x)
        x=re.sub(self.replaceLine,"\n",x)
        x=re.sub(self.replaceTD,"\t",x)
        return x.strip()
        
class NGADOTA:
    def __init__(self,baseUrl,fid,floorTag):
        self.baseUrl=baseUrl
        self.fid=str(fid)
        self.tool=Tool()
        self.DefaultTitle=u'NGA社区'
        self.floorTag=floorTag
        self.floor=1
        self.file=None

    def getPage(self):
        try:
            url=self.baseUrl+self.fid
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            return response.read().decode('gbk').encode('utf-8')
            #return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'连接NGA失败，错误原因',e.reason
                return None

    def getTitle(self):
        page=self.getPage()
        pattern=re.compile('<title>.*?</title>',re.S)
        result=re.search(pattern,page)
        if result:
            print self.tool.replace(result.group().strip())
            return self.tool.replace(result.group().strip())
        else:
            return None

    def getContent(self):
        page=self.getPage()
        pattern=re.compile("<a href='/read.php.*?>(.*?)</a>",re.S)
        items=re.findall(pattern,page)
        contents=[]
        for item in items:
            content='\n'+self.tool.replace(item)+'\n'
            contents.append(content.decode('utf-8'))
                            
        return contents
        '''
        contents=[]
        for item in items:
            content=
            contents.append(content.encode('utf-8'))
        return contents
        '''

    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+'.txt','w+')
        else:
            self.file=open(self.DefaultTitle+'.txt','w+')

    def writeData(self,contents):
        for item in contents:
            if self.floorTag=='1':
                floorLine='\n'+str(self.floor)+u'--------------------------------------------\n'
                self.file.write(floorLine)
            self.file.write(item)
            self.floor+=1

    def start(self):
        indexPage=self.getPage()
        title=self.getTitle()
        self.setFileTitle(title)
        try:
            print u'正在写入数据'
            contents=self.getContent()
            self.writeData(contents)
        except IOError,e:
            print u'写入异常，原因'+e.message
        finally:
            print u'写入任务完成'

baseUrl='http://bbs.ngacn.cc/thread.php?fid='
dota=NGADOTA(baseUrl,321,1)
dota.start()
