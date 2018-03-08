import gevent, time
from urllib import request
from gevent import monkey


monkey.patch_all()#把当前所有的IO操作都做上标记
def f(url):
    print('GET:%s'%url)
    resp = request.urlopen(url)#传链接
    date = resp.read()#读取链接中的数据
    print('%d bytes reveived from %s'%(len(date), url))


urls=['http://www.python.org/',
          'http://www.yahoo.com/',
          'http://www.giyhub.com/'
    ]
gevent.joinall([
    gevent.spawn(f, 'http://www.python.org/'),
    gevent.spawn(f, 'http://www.yahoo.com/'),
    gevent.spawn(f, 'http://www.giyhub.com/'),

    ])