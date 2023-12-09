import toml
from data_fetch import fetch_repo_data
from filter_commits import filter_commits
from count_contributors import count_contributors

def main():
    # Load the TOML file
    with open('aptosRepos.toml', 'r') as file:
        data = toml.load(file)

    # Extract repository URLs - limit to first 20
    repo_urls = [repo['url'] for repo in data['repo']][:20]

    # Iterate over each repository URL
    for repo_url in repo_urls:
        try:
            # Fetch commit and contributor data
            commits, contributors = fetch_repo_data(repo_url)

            # Filter commits
            filtered_commits = filter_commits(commits)

            # Count contributors
            total_commits, full_time, part_time, one_time = count_contributors(filtered_commits)

            # Print the results
            print("Repository:", repo_url)
            print("Total Commits:", len(filtered_commits))
            print("Full-Time Contributors:", full_time)
            print("Part-Time Contributors:", part_time)
            print("One-Time Contributors:", one_time)
            print()

        except Exception as e:
            print(f"Error processing repository {repo_url}: {e}")

if __name__ == "__main__":
    main()
