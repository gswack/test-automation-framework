from flask import Blueprint, render_template
import logging

from services.github import get_github_builds
from services.jenkins import get_jenkins_builds

routes = Blueprint('routes', __name__)


@routes.route('/')
def dashboard():
    try:
        github_data = get_github_builds()
        jenkins_data = get_jenkins_builds()
        return render_template("dashboard.html",
                               github=github_data,
                               jenkins=jenkins_data)
    except Exception as e:
        logging.exception(f"Error handling request: {e}")
        return "An error occurred while processing your request", 500


@routes.route('/health')
def health():
    return "OK", 200
