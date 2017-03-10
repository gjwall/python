#!C:\python36\python.exe

'''
Created on 10 Mar 2017

@author: Graham
'''

import socketserver
import http.server

PORT = 8080

handsy = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), handsy)

httpd.serve_forever()



