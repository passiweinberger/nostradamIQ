#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flup.server.fcgi import WSGIServer
from cgi import parse_qs
import requests
import base64
import datetime
from tinydb import TinyDB, where

FILTER = False
CACHE_MIN = 5


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    url = "No url given"
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
    #print(datetime.datetime.today().timestamp())
    ago = datetime.datetime.now() - datetime.timedelta(minutes=CACHE_MIN)
    ago = int((ago-datetime.datetime(1970,1,1)).total_seconds())#.timestamp())
    print(ago)
    db.remove(where('date') < ago)
    search = db.search((where('url') == url) & (where('date') > ago))
    #print()
    if len(search) > 0:
        cached = True
    if cached:
        #print(search)
        return base64.b64decode(search[0]['content'])
    else:
        req = requests.get(url)
        date = int((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds())#.timestamp())
        db.insert({'url':url,'date':date, 'content':base64.b64encode(req.content)})
        return req.content


WSGIServer(app).run()

"""
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, app)
    srv.serve_forever()
"""
