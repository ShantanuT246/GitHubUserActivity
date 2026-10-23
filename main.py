import sys
import urllib.request
import urllib.error
import json
import os

URL_BASE = "https://api.github.com/users/"
URL_ENDPOINT = "/events"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def getUser():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        raise ValueError("Username not provided. Usage: python script.py <username>")

def requestToGitHub(username: str):
    url = URL_BASE + username + URL_ENDPOINT
    
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return body
    except urllib.error.HTTPError as e:
        print(f"HTTP Error occurred!")
        print(f"Status Code: {e.code}")      
        print(f"Reason: {e.reason}")
        if e.code == 403:
            print("Hint: Rate limit exceeded. Make sure your GITHUB_TOKEN environment variable is set.")
    except urllib.error.URLError as e:
        print(f"Failed to reach the server. Reason: {e.reason}")
        
    return None

def jsonPayload(body):
    events = json.loads(body)
    
    if not events:
        print("No recent activity found.")
        return

    for event in events:
        eventType = event.get("type")
        repoName = event.get("repo", {}).get("name", "Unknown Repository")
        
        if eventType == "PushEvent":
            commits = event.get("payload", {}).get("size", 0)
            print(f"Pushed {commits} commits to {repoName}")
        elif eventType == "WatchEvent":
            print(f"Starred {repoName}")
        elif eventType == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "repository")
            print(f"Created {ref_type} in {repoName}")
        elif eventType == "IssuesEvent":
            action = event.get("payload", {}).get("action", "interacted with")
            print(f"{action.capitalize()} an issue in {repoName}")
        else:
            
            print(f"{eventType.replace('Event', '')} action in {repoName}")

def main():
    try:
        username = getUser()
        print(f"Fetching activity for {username}...\n")
        body = requestToGitHub(username)
        if body:
            jsonPayload(body)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()