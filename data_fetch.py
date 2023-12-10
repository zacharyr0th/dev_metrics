"""
Module docstring: A module to fetch repository data from GitHub.
"""

import time
import os
import requests

def fetch_repo_data(repo_url):
    """
    Fetches commit data for a given GitHub repository.

    Args:
        repo_url (str): The URL of the GitHub repository.

    Returns:
        tuple: A tuple containing a list of all commits and an empty list.
    """
    github_pat = os.getenv('GITHUB_PAT')  # Load GitHub PAT from environment variable
    headers = {'Authorization': f'token {github_pat}'}
    repo_name = '/'.join(repo_url.split('/')[-2:])
    commits_url = f'https://api.github.com/repos/{repo_name}/commits'

    all_commits = []

    while True:
        try:
            # Added timeout argument to the requests.get method
            response = requests.get(commits_url, headers=headers, timeout=10)

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
