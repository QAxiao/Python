import functools

def log(text,text1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s()' %(text,func.__name__)
            r=func()
            print '%s %s()' %(text1,func.__name__)
            return r
        return wrapper
    return decorator

@log('begin call','end call')
def now():
    print '2015-6-1'
    
f=now()
