#!/usr/bin/env python
#-*- coding:utf-8 -*-

true_num=23
k=1
while k<6:
    guess_num=raw_input("\n请输入数字".decode('utf-8').encode('gbk'))
    if guess_num.isdigit():
        guess_num=int(guess_num)
        if guess_num>true_num:
            print u"您猜的数字太大了!"
            k+=1
        elif guess_num<true_num:
            print u"您猜的数字太小了!"
            k+=1
        else:
            print u"Amazing! 你猜到正确的数字了，你用了%d次机会!"%k
            break
    else:
        print u"请输入数字, 而不是输入字符..."
        k+=1
        
if k==6:
    print u"抱歉，你没有尝试的机会了~~~~(>_<)~~~~"

print "Game Over"
