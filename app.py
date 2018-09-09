# -*- coding: utf-8 -*-

import os
from os import environ as env
import bottle
application = bottle.default_app()
from bottle import default_app, request, route, response, get
from sys import argv

bottle.debug(True)

@route('/')
def redir():
    redirect('/home')
@route('/<name>')
def index(name):
    if name == 'home':
        return '<h1>Home</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    elif name == 'about':
        return '<h1>About</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    elif name == 'contact':
        return '<h1>Contact</h1>' \
               '<a href="/home">Home</a><br><a href="/about">About</a><br><a href="/contact">Contact</a>'
    else:
        abort(404)
@error(404)
def error404(error):
    return '<h1>villa</h1>'

"""@route('/')
def redir():
    redirect('/path?id=1')
@route('/path')
def index():
    id = request.query.id
    if  id == '1':
        return '<h1>Home</h1>' \
               '<link rel="stylesheet" href="static/css/style.css">' \
               '<a href="/path?id=1"><img src="static/img/shib1.jpg"></a><br><a href="/path?id=2"><img src="static/img/shib2.jpg"></a><br><a href="/path?id=3"><img src="static/img/shib3.jpg"></a>'
    elif id == '2':
        return '<h1>About</h1>' \
               '<link rel="stylesheet" href="static/css/style.css">' \
               '<a href="/path?id=1"><img src="static/img/shib2.jpg"></a><br><a href="/path?id=2"><img src="static/img/shib1.jpg"></a><br><a href="/path?id=3"><img src="static/img/shib3.jpg"></a>'
    elif id == '3':
        return '<h1>Contact</h1>' \
               '<link rel="stylesheet" href="static/css/style.css">' \
               '<a href="/path?id=1"><img src="static/img/shib3.jpg"></a><br><a href="/path?id=1"><img src="static/img/shib1.jpg"></a><br><a href="/path?id=3"><img src="static/img/shib2.jpg"></a>'
    else:
        abort(404)
@error(404)
def error404(error):
    return '<h1>villa</h1>'
@route('/static/<skra:path>')
def static_skrar(skra):
    return static_file(skra, root='./public/')"""

bottle.run(host='0.0.0.0', port=argv[1])
