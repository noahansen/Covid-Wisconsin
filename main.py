import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)
# df = pd.read_csv("main.csv") #data

@app.route('/')
def home():
    return render_template("plots.html")
    #or jsut return graph.toHtml

if __name__ == '__main__':
    app.run(host="0.0.0.0") 
