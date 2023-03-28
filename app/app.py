from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    name = request.cookies.get('form')
    return f'Hello {name}!'
