from flask import Flask
import pendulum
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/time")
def current_time():
    ist = pendulum.timezone('Asia/Calcutta')
    now = datetime.now(ist)
    current_time = now.strftime("%H:%M:%S")
    return (current_time)


