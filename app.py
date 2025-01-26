from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

###WSGI APPLICATION 
app = Flask(__name__)

@app.route('/')
def learning():
    return 'Learning flask want to becom data scientist '

@app.route('/index')
def index():
    return "leanring new thing are amazing"

if __name__ == '__main__':
    app.run(debug=True)