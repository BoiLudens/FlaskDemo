from flask import request, render_template
from . import hello

@hello.route('/', methods=['GET'])
def index():
    return 'Hello World'