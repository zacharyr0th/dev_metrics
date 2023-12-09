from datetime import datetime
from collections import defaultdict
import logging

def count_contributors(commits, full_time_threshold=10):
    total_commits = len(commits)
    contribution_days = defaultdict(set)

    for commit in commits:
        try:
            author = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
            date_str = commit.get('commit', {}).get('author', {}).get('date', '')

            if date_str:
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').date()
                contribution_days[author].add(date)
        except Exception as e:
            logging.error(f"Error processing commit for contributor count (Author: {author}): {e}")

    full_time_contributors = 0
    part_time_contributors = 0
    one_time_contributors = 0

    for days in contribution_days.values():
        days_count = len(days)
        if days_count >= full_time_threshold:
            full_time_contributors += 1
        elif 1 <= days_count < full_time_threshold:
            part_time_contributors += 1
        elif days_count == 1:
            one_time_contributors += 1

    return total_commits, full_time_contributors, part_time_contributors, one_time_contributors
