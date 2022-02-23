#Student Name: Paul Thottappilly
#Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam

#importing necessary imports
from flask import Flask, render_template, request

#creates flask app
app = Flask(__name__)

#creates a function to render the home page
@app.route('/')
def home():
    return render_template('home.html')

#creates a function to render the calculation page
@app.route('/calculate')
def calc(numb=None):
    if len(request.args)==0:
        return render_template('calculate.html')
    numb = request.args['number']
    try:
        if int(numb)%2==0:
            msg='even'
        elif int(numb)%2!=0:
            msg='odd'
    except:
        msg='not an integer!'
    return render_template('calculate.html', num=numb, name=msg)

if __name__ == "__main__":
    app.run()