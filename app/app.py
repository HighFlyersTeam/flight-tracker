from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
