import requests


def get_github_builds():
    token = "YOUR_GITHUB_TOKEN"
    repo = "gswack/test-automation-framework"
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{repo}/actions/runs"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        runs = response.json().get("workflow_runs", [])
        return [{
            "name": run["name"],
            "status": run["status"],
            "conclusion": run["conclusion"],
            "created_at": run["created_at"]
        } for run in runs[:5]]
    except Exception as e:
        print(f"GitHub API error: {e}")
        return []
