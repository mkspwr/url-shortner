from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return'This is Vihaan URL shortener'
@app.route('/your-url')
def your_url():
    return render_template('your_url.html')