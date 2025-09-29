import os
import logging
from flask import Flask

from app.routes import routes


app = Flask(__name__)
app.register_blueprint(routes)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')


@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404


@app.errorhandler(500)
def internal_error(e):
    return "Internal server error", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
