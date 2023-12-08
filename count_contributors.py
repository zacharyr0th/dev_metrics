from datetime import datetime
from collections import defaultdict

def count_contributors(commits):
    total_commits = len(commits)
    contribution_days = defaultdict(set)

    for commit in commits:
        try:
            author = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
            date_str = commit.get('commit', {}).get('author', {}).get('date', '')
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').date()
            contribution_days[author].add(date)
        except Exception as e:
            print(f"Error processing commit for contributor count: {e}")

    full_time_contributors = 0
    part_time_contributors = 0
    one_time_contributors = 0

    for days in contribution_days.values():
        if len(days) >= 10:
            full_time_contributors += 1
        elif 1 <= len(days) < 10:
            part_time_contributors += 1
        elif len(days) == 1:
            one_time_contributors += 1

    return total_commits, full_time_contributors, part_time_contributors, one_time_contributors
