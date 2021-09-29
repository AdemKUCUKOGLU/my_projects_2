from flask import Flask
from werkzeug.utils import format_string

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return "Bize her yer trabzon"

@app.route('/third/subthird')
def third():
    return "Bu sayfa üçüncü sayfanın alt sayfasıdır..."

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'id number of this page is {id}'

if __name__ == '__main__':
    app.run(debug=True)