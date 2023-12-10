"""
Module docstring: This script analyzes repository data to count 
contributors based on commit history.
"""

import logging
import toml  # standard import "import toml" should be placed before "import logging"
from data_fetch import fetch_repo_data
from filter_commits import filter_commits
from count_contributors import count_contributors

def main():
    """Main function to orchestrate data fetching, 
    filtering and counting operations."""
    # Initialize logging with the appropriate format and level
    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # Load configuration from TOML file
    with open('aptos_repos.toml', encoding='utf-8') as file:  # Specify encoding explicitly
        data = toml.load(file)
    # Extract repository URLs
    repo_urls = [repo['url'] for repo in data['repo']]
    # Initialize cumulative counters
    cumulative_commits = 0
    cumulative_full_time = 0
    cumulative_part_time = 0
    cumulative_one_time = 0

    for repo_url in repo_urls:
        try:
            # Fetch commit and contributor data
            commits, _ = fetch_repo_data(repo_url)
            # Filter commits
            filtered_commits = filter_commits(commits)
            # Count contributors
            _, full_time, part_time, one_time = count_contributors(filtered_commits)
            # Accumulate the results
            cumulative_commits += len(filtered_commits)
            cumulative_full_time += full_time
            cumulative_part_time += part_time
            cumulative_one_time += one_time
            # Print the results for each repository
            logging.info("Repository: %s", repo_url)
            logging.info("Total Commits: %d", len(filtered_commits))
            logging.info("Full-Time Contributors: %d", full_time)
            logging.info("Part-Time Contributors: %d", part_time)
            logging.info("One-Time Contributors: %d", one_time)

        except Exception as e:
            logging.error("Unexpected error processing repository '%s': %s", repo_url, e)

    # Print cumulative results
    logging.info("Cumulative Results:")
    logging.info("Total Commits: %d", cumulative_commits)
    logging.info("Full-Time Contributors: %d", cumulative_full_time)
    logging.info("Part-Time Contributors: %d", cumulative_part_time)
    logging.info("One-Time Contributors: %d", cumulative_one_time)

if __name__ == "__main__":
    main()
