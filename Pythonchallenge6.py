import zipfile
import re

'''
if __name__=="__main__":
    z=zipfile.ZipFile('channel.zip',mode='r')
    prefix='90052'
    surfix='.txt'

    findNothing=re.compile('Next nothing is (\d*)').search

    comments=[]

    while True:
        text=z.read(prefix+surfix);
        print(text)

        match=findNothing(text)

        if match:
            prefix=match.group(1)
            print 'group(0) is '+match.group(0)
            print 'group(1) is '+match.group(1)
            comments.append(z.getinfo(prefix+surfix).comment)
        else:
            break

    print "".join(comments)
'''
z=zipfile.ZipFile('channel.zip',mode='r')
name = '90052.txt'
while 1:
    print z.getinfo(name).comment,
    name = z.read(name).split()[-1] + '.txt'
