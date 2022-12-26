#import flask package
from flask import Flask

app = Flask(__name__)

#Set up main page and two additional pages
@app.route('/')
def home_page():
    return 'Hello world!'

@app.route('/dashboard')
def dashboard():
    return 'This is my new dashboard page'

@app.route('/details')
def details():
    return 'This is the details page'

#Run app with command 'python app.py' 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)