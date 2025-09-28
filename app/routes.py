from flask import Blueprint, request
import logging
import datetime


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    try: 
        timestamp = datetime.datetime.now().isoformat()
        client_ip = request.remote_addr
        message = f"Hello, you are IP {client_ip}"
        logging.info(message)
        return f"Hello, {message}"
    except Exception as e:
        logging.exception(f"Error handling request: {e}")
        return "An error occurred while processing your request", 500
    

@routes.route('/health')
def health():
    return "OK", 200
