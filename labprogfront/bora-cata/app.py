from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/download")
def download():
    return render_template ("download.html")
