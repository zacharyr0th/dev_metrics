import toml
import csv
from data_fetch import fetch_repo_data
from filter_commits import filter_commits
from count_contributors import count_contributors

def main():
    # Load the TOML file
    with open('aptosRepos.toml', 'r') as file:
        data = toml.load(file)

    # Extract repository URLs - limit to first 20
    repo_urls = [repo['url'] for repo in data['repo']][:20]

    # Open a file to save the results
    with open('results.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(['Repository', 'Total Commits', 'Full-Time Contributors', 'Part-Time Contributors', 'One-Time Contributors'])

        # Iterate over each repository URL
        for repo_url in repo_urls:
            try:
                # Fetch commit and contributor data
                commits, contributors = fetch_repo_data(repo_url)

                # Filter commits
                filtered_commits = filter_commits(commits)

                # Count contributors
                total_commits, full_time, part_time, one_time = count_contributors(filtered_commits)

                # Write the results to the CSV file
                csvwriter.writerow([repo_url, len(filtered_commits), full_time, part_time, one_time])

            except Exception as e:
                print(f"Error processing repository {repo_url}: {e}")

'''
the following is to iterate through the entire aptosRepos.toml file - takes forever with GH's rate limiting

def main():
    # Load the TOML file
    with open('aptosRepos.toml', 'r') as file:
        data = toml.load(file)

    # Extract repository URLs
    repo_urls = [repo['url'] for repo in data['repo']]

    # Open a file to save the results
    with open('results.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header row
        csvwriter.writerow(['Repository', 'Total Commits', 'Full-Time Contributors', 'Part-Time Contributors', 'One-Time Contributors'])

        # Iterate over each repository URL
        for repo_url in repo_urls:
            try:
                # Fetch commit and contributor data
                commits, contributors = fetch_repo_data(repo_url)

                # Filter commits
                filtered_commits = filter_commits(commits)

                # Count contributors
                total_commits, full_time, part_time, one_time = count_contributors(filtered_commits)

                # Write the results to the CSV file
                csvwriter.writerow([repo_url, len(filtered_commits), full_time, part_time, one_time])

            except Exception as e:
                print(f"Error processing repository {repo_url}: {e}")
'''             
if __name__ == "__main__":
    main()
