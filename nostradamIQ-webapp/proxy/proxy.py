#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flup.server.fcgi import WSGIServer
from cgi import parse_qs
import requests
import base64
import datetime
from tinydb import TinyDB, where
import urllib
import urllib2
from urlparse import urlparse

FILTER = False
CACHE_MIN = 5


def makeUrlRequest(url):
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
    url_parsed = urlparse(url)
    referer = str(urlparsed.scheme) + str(url_parsed.netloc)
    headers = { 'User-Agent' : user_agent,
                'Referer': referer,
                'Origin': origin, 
                'Access-Control-Allow-Origin': '*' }
    req = urllib2.Request(url, headers)
    response = urllib2.(req)
    response.addHeader('Access-Control-Allow-Origin': '*') 
    #content = response.read()
    return response #content


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    url = "No URL given"
    if 'url' in parameters:
        url = parameters['url'][0]
        valid = True
        if FILTER == True:
            with open('urls.txt') as f:
                urls = f.read().splitlines()
            if url not in urls:
                valid = False
        print(url)
        if valid:
            return getDocByUrl(url)
    return ""


def getDocByUrl(url):
    cached = False
    db = TinyDB('cache.json')
    ago = int(((datetime.datetime.now() - datetime.timedelta(minutes=CACHE_MIN)) - datetime.datetime(1970,1,1)).total_seconds()) #.timestamp())
    #print(ago)
    db.remove(where('date') < ago)
    search = db.search((where('url') == url) & (where('date') > ago))
    if len(search) > 0:
        cached = True
    if cached:
        #print(search)
        return base64.b64decode(search[0]['content'])
    else:
        req = makeUrlRequest(url) #requests.get(url) #set headers
        content = req.read()
        date = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()) #.timestamp())
        db.insert({'url':url,'date':date, 'content':base64.b64encode(content)})
        return content


WSGIServer(app).run()

"""
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, app)
    srv.serve_forever()
"""
