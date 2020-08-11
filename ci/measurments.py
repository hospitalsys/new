from requests import get
import json

auth_user = "nabaryasia2@gmail.com"
auth_pass = "301901567asia"

project = "hospitalsys"
repository = "projectFiles"

api_endpoint = "https://api.github.com/repos/%s/%s" % (project, repository)

headers = {
    "accept": "application/vnd.github.v3+json"
}

teams = {
    "team1": {
        "assignee": "asiana-nabary"
    },
    "team2": {
        "assingee": "AsiaNabary"
#                "owner": "nabaryasia2"

    },
    "team3": {
        "assignee": "hurarabin2020" 
#             "owner": "yonesheba200",
#                        "owner": "nooralquranhura"


    },
    "team4": {
        "assignee": "schoolcom20hura"
    }
}

for team in teams:
    print("Closed issues for team: %s" % team)
    url = api_endpoint + "/issues?assignee=%s&state=closed" % teams[team]["assignee"]
    resp = get(url, auth=(auth_user, auth_pass), headers=headers).json()
    print("    %s" % len(resp))

    print("Open bugs for team: %s" % team)
    url = api_endpoint + "/issues?assignee=%s&state=open&labels=bug" % teams[team]["assignee"]
    resp = get(url, auth=(auth_user, auth_pass), headers=headers).json()
    print("    %s" % len(resp))

    print("Failed deployments for team: %s" % team)
    url = api_endpoint + "/actions/runs?conclusion=failiure&assignee=%s" % teams[team]["assignee"]
    resp = get(url, headers=headers).json()
    print("    %s" % resp["total_count"])
