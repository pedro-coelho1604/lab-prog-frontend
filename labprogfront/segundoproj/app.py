from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return"<h1>Pagode programa em HTML<\h1>"

