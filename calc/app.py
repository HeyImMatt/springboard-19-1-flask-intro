from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = request.args['a']
    b = request.args['b']
    result = add(int(a), int(b))
    return f'{result}'

@app.route('/sub')
def sub_route():
    a = request.args['a']
    b = request.args['b']
    result = sub(int(a), int(b))
    return f'{result}'

@app.route('/mult')
def mult_route():
    a = request.args['a']
    b = request.args['b']
    result = mult(int(a), int(b))
    return f'{result}'

@app.route('/div')
def div_route():
    a = request.args['a']
    b = request.args['b']
    result = div(int(a), int(b))
    return f'{result}'

      
@app.route('/math/<op>')
def math_route(op):
    math_funcs = {
      'add': add, 
      'sub': sub,
      'mult': mult,
      'div': div,
      }
    a = request.args['a']
    b = request.args['b']
    result = math_funcs[op](int(a), int(b))
    return f'{result}'