# -*- coding: utf-8 -*-
"""
Created on Sun September 28 2025

@author: gswack
"""

import requests
from requests.auth import HTTPBasicAuth


def get_jenkins_builds() -> list:
    jenkins_url = "http://your-jenkins-url/job/your-job-name/api/json"
    username = "gswack"
    token = "your-api-token"

    try:
        response = requests.get(jenkins_url, auth=HTTPBasicAuth(username, token))
        response.raise_for_status()
        builds = response.json().get("builds", [])
        return [{
            "number": build["number"],
            "url": build["url"],
            "result": build.get("result"),
            "timestamp": build["timestamp"]
        } for build in builds[:5]]
    except Exception as e:
        print(f"Jenkins API error: {e}")
        return []
