from .main import app
from flask import Flask, request, render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/whats_my_ip")
def whats_my_ip():
    return render_template('ip.html', ip=request.remote_addr)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
