irrelevant_keywords = ['merge pull request', 'library update', 'dependency update'] 

def filter_commits(commits):
    filtered_commits = []
    for commit in commits:
        try:
            # Handle different commit structures
            if isinstance(commit, dict) and 'commit' in commit and isinstance(commit['commit'], dict) and 'message' in commit['commit']:
                message = commit['commit']['message'].lower()
                if not any(keyword in message for keyword in irrelevant_keywords):
                    filtered_commits.append(commit)
            else:
                print(f"Unexpected commit format: {commit}")
        except Exception as e:
            print(f"Error filtering commit: {e}")
    return filtered_commits
