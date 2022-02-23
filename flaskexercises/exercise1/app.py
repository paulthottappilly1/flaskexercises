#Student Name: Paul Thottappilly
#Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam

#importing necessary imports
from flask import Flask, render_template
import calendar
import datetime

#creates flask app
app = Flask(__name__)

#creates a function that retrieves the time  
@app.route('/')
def index():
    currenttime = datetime.datetime.now()
    ctime = currenttime.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', ctime = calendar.day_name[currenttime.weekday()] + ', ' +ctime)

if __name__ == '__main__':
    app.run()
