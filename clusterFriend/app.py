# A little app that will use fortune on the system to give you a fortune and some network info.
# Designed for testing cluster services (you can just make a simple request and prove it's clustering!)
# --Easton Pillay.

from flask import Flask, redirect
from datetime import datetime
import pprint
import socket
import subprocess
import urllib.request

app = Flask(__name__)

@app.route('/api')
def fortune():
    time = str(datetime.today())
    result = subprocess.check_output("fortune", shell=True, text=True)
    hostname = socket.gethostname()
    internalIP = socket.gethostbyname(hostname)
    externalIP = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    # cleaned = result.replace('\t', '  ').replace('\n', '')
    return {
        "time": time,
        "fortune": result,
        "hostname": hostname,
        "external_ip": externalIP,
        "internal_ip": internalIP
    }
@app.route('/')
def index():
    return redirect('/api')