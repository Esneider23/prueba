from http import server
from flask import Flask

server = Flask(__name__)

@server.route('/')
def hola():
    return "Saludo desde Flask..."


if __name__ == '__main__':
    server.run()