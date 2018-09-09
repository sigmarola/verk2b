# -*- coding: utf-8 -*-

import os
from os import environ as env
import bottle
application = bottle.default_app()
from bottle import default_app, request, route, response, get
from sys import argv

bottle.debug(True)


@get('/')
def home():
    return """<!DOCTYPE html>
            <html>
            <head>
                <title>Verk1</title>
            </head>
            <body>
                <h1>Halló heimur</h1>
                <a href="https://github.com/sigmarola/verk1">Github</a>
            </body>
            </html>"""




bottle.run(host='0.0.0.0', port=argv[1])
