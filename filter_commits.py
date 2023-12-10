"""
This module filters commits by removing those that contain irrelevant keywords.
"""

import logging

def filter_commits(commits, keywords=None):
    """
    Filters commits to exclude those that contain any of the specified keywords.

    Args:
        commits (list): A list of commit dictionaries.
        keywords (list): A list of keywords to filter out. Defaults to a predefined list.

    Returns:
        list: The list of filtered commits.
    """
    if keywords is None:
        keywords = ['merge pull request', 'library update', 'dependency update']
    filtered_commits = []
    for commit in commits:
        try:
            message = commit.get('commit', {}).get('message', '').lower()
            if not any(keyword in message for keyword in keywords):
                filtered_commits.append(commit)
        except KeyError as ke:
            logging.error("Key error filtering commit: %s", ke)
    return filtered_commits
