from flask import render_template, Blueprint
import time
import psutil

server_bp = Blueprint('server', __name__)

@server_bp.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@server_bp.route('/apistatus', methods=['GET'])
def status():
    api_status = {
        "status": "online",
        "version": "1.0",
        "description": "Status Check",
    }
    server_info = {
        "uptime": int(time.time() - psutil.boot_time()),  
        "cpu_usage_percent": psutil.cpu_percent(),  
        "memory_usage_percent": psutil.virtual_memory().percent,  
    }

    return {
        "api_status": api_status,
        "server_info": server_info
    }, 201