from requests import get

auth_user = "username"
auth_pass = "password"

project = "proj"
repository = "repo"

api_endpoint = "https://api.github.com/repos/%s/%s" % (project, repository)

headers = {
    "accept": "application/vnd.github.v3+json"
}

teams = {
    "team1": {
        "users": ["u1", "u2", "u3"],
        "owner": "u1"
    },
    "team2": {
        "users": ["u3", "u4", "u5"],
        "owner": "u3"
    },
    "team3": {
        "users": ["u6", "u7", "u8"],
        "owner": "u6"
    },
    "team4": {
        "users": ["u9", "u10", "u11"],
        "owner": "u9"
    }
}

for team in teams:
    print("Closed issues for team: %s" % team)
    url = api_endpoint + "/issues?owner=%s&state=closed" % teams[team]["owner"]
    resp = get(url, auth=(auth_user, auth_pass), headers=headers).json()
    print("    %s" % len(resp))

    print("Open bugs for team: %s" % team)
    url = api_endpoint + "/issues?owner=%s&state=open&labels=bug" % teams[team]["owner"]
    resp = get(url, auth=(auth_user, auth_pass), headers=headers).json()
    print("    %s" % len(resp))

    print("Failed deployments for team: %s" % team)
    url = api_endpoint + "/actions/runs?conclusion=failiure&owner=%s" % teams[team]["owner"]
    resp = get(url, auth=(auth_user, auth_pass), headers=headers).json()
    print("    %s" % resp["total_count"])
