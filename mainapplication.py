from flask import Flask

app=Flask(__name__)


print("Name - " + __name__)

@app.route('/')
def home():
    return "<html> Hello Vihaan!</html>"