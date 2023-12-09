import logging

irrelevant_keywords = ['merge pull request', 'library update', 'dependency update'] 

def filter_commits(commits, keywords=irrelevant_keywords):
    filtered_commits = []
    for commit in commits:
        try:
            message = commit.get('commit', {}).get('message', '').lower()
            if not any(keyword in message for keyword in keywords):
                filtered_commits.append(commit)
        except Exception as e:
            logging.error(f"Error filtering commit: {e}")
    return filtered_commits
