#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
 
import os
import ssl
import sys
import json
import time
import base64
# import psutil
 
 
from urllib.request import Request, urlopen
from urllib.error import URLError
 
INSECURE_CONTEXT = ssl._create_unverified_context()
 
 
def api(url, method=None, data=None, token=None, username=None, password=None):
 
    if data:
        params = json.dumps(data).encode('utf8')
        req = Request(url, data=params, headers={'Content-Type': 'application/json; charset=utf-8','Cache-Control': 'no-cache'})
   
    else:
        req = Request(url, headers={'Cache-Control': 'no-cache'})
 
    if method:
        req.get_method = lambda: method
 
    else:
        req.get_method = lambda: 'GET'
 
    if token:
        req.add_header("Authorization", "Bearer %s" % token)
 
    else:
        if username and password:
            credentials = ('%s:%s' % (username, password))
            encoded_credentials = base64.b64encode(credentials.encode('utf8'))
            req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("utf8"))
 
    try:
        with urlopen(req, timeout=10, context=INSECURE_CONTEXT) as response:
            res = response.read()
 
        if not res:
            return True
 
        else:
            return json.loads(res.decode("utf-8"))
 
    except:
   
        return False
 
def main():
 
    pass
 
 
if __name__ == '__main__':
 
    sys.exit(main())
