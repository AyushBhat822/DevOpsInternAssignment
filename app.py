from flask import Flask
import pendulum
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route("/")
@metrics.do_not_track()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/time")
def current_time():
    ist = pendulum.timezone('Asia/Calcutta')
    now = datetime.now(ist)
    current_time = now.strftime("%H:%M:%S")
    return (current_time)

if __name__ == '__main__':
    app.run()