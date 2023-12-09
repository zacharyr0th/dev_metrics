import toml
import logging
from data_fetch import fetch_repo_data
from filter_commits import filter_commits
from count_contributors import count_contributors

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Initialize logging
    with open('aptosRepos.toml', 'r') as file: # Load the TOML file
        data = toml.load(file)

    # Extract repository URLs - limit to first 20 for testing
    # repo_urls = [repo['url'] for repo in data['repo']][:20] 

    # Extract all repository URLs
    repo_urls = [repo['url'] for repo in data['repo']]

    for repo_url in repo_urls: # Iterate over each repository URL
        try:
            commits, contributors = fetch_repo_data(repo_url) # Fetch commit and contributor data
            filtered_commits = filter_commits(commits) # Filter commits
            total_commits, full_time, part_time, one_time = count_contributors(filtered_commits) # Count contributors

            # Print the results
            logging.info(f"Repository: {repo_url}")
            logging.info(f"Total Commits: {len(filtered_commits)}")
            logging.info(f"Full-Time Contributors: {full_time}")
            logging.info(f"Part-Time Contributors: {part_time}")
            logging.info(f"One-Time Contributors: {one_time}")

        except Exception as e:
            logging.error(f"Error processing repository {repo_url}: {e}")

if __name__ == "__main__":
    main()
