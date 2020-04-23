import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)
# df = pd.read_csv("main.csv") #data

@app.route('/')
def home():
    return render_template("index.html")
    #or jsut return graph.toHtml

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/acks')
def acks():
    return render_template("acks.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0") 
