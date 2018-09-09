# -*- coding: utf-8 -*-

import os
from os import environ as env
import bottle
application = bottle.default_app()
from bottle import default_app, request, route, response, get
from sys import argv

bottle.debug(True)


@get('/<name>')
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


bottle.run(host='0.0.0.0', port=argv[1])
