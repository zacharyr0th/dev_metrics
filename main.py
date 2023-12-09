import toml
import logging
from data_fetch import fetch_repo_data
from filter_commits import filter_commits
from count_contributors import count_contributors

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Initialize logging
    with open('aptosRepos.toml', 'r') as file: # Load the TOML file
        data = toml.load(file)

    # Extract all repository URLs
    repo_urls = [repo['url'] for repo in data['repo']]

    # Initialize cumulative counters
    cumulative_commits = 0
    cumulative_full_time = 0
    cumulative_part_time = 0
    cumulative_one_time = 0

    for repo_url in repo_urls: # Iterate over each repository URL
        try:
            commits, contributors = fetch_repo_data(repo_url) # Fetch commit and contributor data
            filtered_commits = filter_commits(commits) # Filter commits
            total_commits, full_time, part_time, one_time = count_contributors(filtered_commits) # Count contributors

            # Accumulate the results
            cumulative_commits += len(filtered_commits)
            cumulative_full_time += full_time
            cumulative_part_time += part_time
            cumulative_one_time += one_time

            # Print the results for each repository
            logging.info(f"Repository: {repo_url}")
            logging.info(f"Total Commits: {len(filtered_commits)}")
            logging.info(f"Full-Time Contributors: {full_time}")
            logging.info(f"Part-Time Contributors: {part_time}")
            logging.info(f"One-Time Contributors: {one_time}")

        except Exception as e:
            logging.error(f"Error processing repository {repo_url}: {e}")

    # Print cumulative results
    logging.info("Cumulative Results:")
    logging.info(f"Total Commits: {cumulative_commits}")
    logging.info(f"Full-Time Contributors: {cumulative_full_time}")
    logging.info(f"Part-Time Contributors: {cumulative_part_time}")
    logging.info(f"One-Time Contributors: {cumulative_one_time}")

if __name__ == "__main__":
    main()
