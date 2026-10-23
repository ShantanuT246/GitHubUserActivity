# GitHub User Activity CLI

A lightweight command-line tool that fetches and displays the recent activity of any GitHub user. This project was built to practice interacting with REST APIs, handling JSON data, and managing HTTP requests using only Python's built-in libraries. 

Based on the [GitHub User Activity project from roadmap.sh](https://roadmap.sh/projects/github-user-activity).

## Features
- Fetches recent public events (up to 30) for a specified GitHub user.
- Parses and formats different types of events (e.g., `PushEvent`, `WatchEvent`, `IssuesEvent`, `CreateEvent`).
- Built entirely with standard Python libraries (`sys`, `urllib`, `json`, `os`)—no external dependencies like `requests` required.
- Handles API rate limits gracefully by supporting Personal Access Tokens via environment variables.

## Prerequisites
- Python 3.x installed on your machine.

## Setup & Usage

1. **Clone or Download the script**
   Save the Python script as `github_activity.py` (or your preferred name) to your local machine.

2. **Set your GitHub Token (Optional but Recommended)**
   To avoid GitHub's strict unauthenticated rate limits (60 requests per hour), generate a Personal Access Token (PAT) on GitHub and set it as an environment variable in your terminal:
   
   **On macOS/Linux:**
   ```bash
   export GITHUB_TOKEN="your_personal_access_token"
   ```
   **On Windows (Command Prompt):**
   ```cmd
   set GITHUB_TOKEN=your_personal_access_token
   ```
   **On Windows (PowerShell):**
   ```powershell
   $env:GITHUB_TOKEN="your_personal_access_token"
   ```

3. **Run the script**
   Execute the script from your terminal, passing the target GitHub username as an argument:
   ```bash
   python github_activity.py <username>
   ```

## Example Output

```text
$ python github_activity.py kamranahmedse
Fetching activity for kamranahmedse...

Pushed 3 commits to kamranahmedse/developer-roadmap
Starred facebook/react
Created branch in kamranahmedse/developer-roadmap
Opened an issue in kamranahmedse/developer-roadmap
```

## Error Handling
The script handles common errors, including:
- **Missing Username:** Prompts the user with usage instructions.
- **User Not Found (404):** Displays a clean error message instead of crashing.
- **Rate Limit Exceeded (403):** Warns the user and suggests adding a token.