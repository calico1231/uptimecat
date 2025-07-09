from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)
    return str(uptime_timedelta)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/uptime')
def api_uptime():
    return jsonify({'uptime': get_uptime()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)