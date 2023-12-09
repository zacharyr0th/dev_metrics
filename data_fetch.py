import requests
import time
import os 

github_pat = os.getenv('GITHUB_PAT') # Load GitHub PAT from environment variable
headers = {'Authorization': f'token {github_pat}'}

def fetch_repo_data(repo_url):
    repo_name = '/'.join(repo_url.split('/')[-2:])
    commits_url = f'https://api.github.com/repos/{repo_name}/commits'

    all_commits = []

    while True:
        try:
            response = requests.get(commits_url, headers=headers)

            # Handle rate limiting
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
                wait_time = max(reset_time - time.time(), 0)
                print(f"Rate limit hit. Waiting for {wait_time} seconds to retry.")
                time.sleep(wait_time)
                continue

            # Handle other errors
            elif response.status_code != 200:
                print(f"Error fetching data for {repo_url}: {response.text}")
                break

            commits = response.json()
            all_commits.extend(commits)

            # Pagination handling
            if 'next' in response.links:
                commits_url = response.links['next']['url']
            else:
                break

        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            break

    return all_commits, []

