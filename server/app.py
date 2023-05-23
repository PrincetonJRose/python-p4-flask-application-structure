#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route( '/custom/<string:message>' )
def custom ( message ) :
    return f'<h1> Hello there! Here is your { message } </h1>'

@app.route( '/words' )
def words ( ) :
    return ['Apple', 'number', 'world', 'Cap']

if __name__ == '__main__' :
    app.run( port = 3000, debug = True )