from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)
    return f"Host uptime: {uptime_timedelta}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)