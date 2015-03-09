# -*- mode: python; coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name='World'):
    return 'Hello {}!\n\n'.format(name)

if __name__ == '__main__':
    app.run()
