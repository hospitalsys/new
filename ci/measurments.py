from requests import get
import json

auth_user = "asiana@ac.sce.ac.il"
auth_pass = "A301901567a"

project = "hospitalsys"
repository = "projectFiles"

api_endpoint = "https://api.github.com/repos/%s/%s" % (project, repository)

headers = {
    "accept": "application/vnd.github.v3+json"
}

teams = {
    "team1": {
        "owner": "asiana-nabary"
    },
    "team2": {
        "owner": "AsiaNabary",
                "owner": "nabaryasia2"

    },
    "team3": {
        "owner": "hurarabin2020" ,
                "owner": "yonesheba200",
                        "owner": "nooralquranhura"


    },
    "team4": {
        "owner": "schoolcom20hura"
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
    resp = get(url, headers=headers).json()
    print("    %s" % resp["total_count"])
