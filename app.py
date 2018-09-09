from bottle import route, run, error, template, redirect, abort, request, static_file
from sys import argv
import os
from os import environ as env
application = bottle.default_app()
@route('/')
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
    return static_file(skra, root='./public/')
bottle.debug(True)
#run(host='localhost', port=8000, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])
