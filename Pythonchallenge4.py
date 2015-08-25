import urllib
import urllib2
import os

data= {}
number = '52899'

for i in range(400):
    data['nothing'] = number
    url_values = urllib.urlencode(data)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    full_url = url + '?' + url_values
    
    foo = urllib2.urlopen(full_url)
    foo = foo.read()
    print foo
    foo = foo.split(" ")
    try:
        number = [i for i in foo if i.isdigit()][0]
    except IndexError:
        if 'Divide' in foo:
            number=str(int(number)/2)
        else:
            os.startfile('http://www.pythonchallenge.com/pc/def/'+foo[0])
            break
