# Import what we need from flask
from flask import Flask, render_template

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def temp():
    return render_template('index.html')

#@app.route('/cow')
#def cow():
#    return 'MOoooOo again!'
