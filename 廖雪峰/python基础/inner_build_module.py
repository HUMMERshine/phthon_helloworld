# encoding:utf-8

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;-entity' % name)

    def handle_charref(self, name):
        print('&#%s;-char' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <!-- --> &nbsp;&#1234;<a href=\"#\">html</a> tutorial...<br>END</p></body></html>')


class PyEventParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._count = 0
        self._events = dict()
        self._flag = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
            self._count += 1
            self._events[self._count] = dict()
            self._flag = 'event-title'
        if tag == 'time':
            self._flag = 'time'
        if tag == 'span' and attrs.__contains__(('class', 'event-location')):
            self._flag = 'event-location'

    def handle_data(self, data):
        if self._flag == 'event-title':
            self._events[self._count][self._flag] = data
        if self._flag == 'time':
            self._events[self._count][self._flag] = data
        if self._flag == 'event-location':
            self._events[self._count][self._flag] = data
        self._flag = None

    def event_list(self):
        print '近期关于Python的会议有：', self._count, '个，具体如下：'
        for event in self._events.values():
            print event['event-title'], '\t', event['time'], '\t', event['event-location']


try:
    parser = PyEventParser()
    #下面两行代码需要导入import urllib,进行解析
    #pypage = urllib.urlopen('https://www.python.org/events/python-events/')
    #pyhtml = pypage.read()
    pyhtml = ''
    with open('a.html', 'r') as f:
        pyhtml = f.read()
        #parser.feed(f.read())
except IOError,e:
    print 'IOError:', e
else:
    parser.feed(pyhtml)
    parser.event_list()



