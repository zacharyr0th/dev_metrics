"""
This module provides functionality to count different categories of contributors
based on their commit history.
"""

from datetime import datetime
from collections import defaultdict
import logging

def count_contributors(commits, full_time_threshold=10):
    """
    Counts the number of full-time, part-time, and one-time contributors based on
    commit history.

    Args:
        commits (list): A list of commit data.
        full_time_threshold (int): The number of days to consider someone a full-time
                                   contributor.

    Returns:
        tuple: A tuple containing the total number of commits and counts of full-time,
               part-time, and one-time contributors.
    """
    total_commits = len(commits)
    contribution_days = defaultdict(set)

    for commit in commits:
        try:
            author = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
            date_str = commit.get('commit', {}).get('author', {}).get('date', '')

            if date_str:
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').date()
                contribution_days[author].add(date)

        except ValueError as ve:
            logging.error(
                "Error processing date format for commit by author %s: %s",
                author, ve
            )
        except KeyError as ke:
            logging.error(
                "Key error processing commit for contributor count: %s", ke
            )

        except Exception as e:
            logging.error(
                "Unexpected error processing commit for contributor count (Author: %s): %s",
                author, e
            )
            raise

    full_time_contributors = 0
    part_time_contributors = 0
    one_time_contributors = 0

    for days in contribution_days.values():
        days_count = len(days)
        if days_count >= full_time_threshold:
            full_time_contributors += 1
        elif 1 < days_count < full_time_threshold:
            part_time_contributors += 1
        elif days_count == 1:
            one_time_contributors += 1

    return (total_commits, full_time_contributors, part_time_contributors,
            one_time_contributors)
