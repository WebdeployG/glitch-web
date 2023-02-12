from flask import Flask, render_template
from time import time, ctime

app = Flask(__name__,static_folder='build/static', template_folder='build')

@app.route('/home/<name>')
def home(name):
    with open('visitor.csv','a') as file:
        file.write(f'{name},{ctime(time())}, \n')
    return 'name registrered'

@app.route('/normal/<name>/<sharebutton>')
def normal(name,sharebutton):
    with open('normal.csv','a') as file:
        file.write(f'{name},{ctime(time())},{sharebutton} \n')
    return 'share button clicked'

@app.route('/outlet/<name>/<sharebutton>')
def outlet(name,sharebutton):
    with open('outlet.csv','a') as file:
        file.write(f'{name},{ctime(time())},{sharebutton} \n')
    return 'outlet share button clicked'

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
