# `dev_metrics` Project README

## Introduction

`dev_metrics` is a tool designed for analyzing development activities within various repositories, particularly those related to the Aptos blockchain. It includes scripts for data fetching, filtering commits, and counting contributors.

## Features

- **Commit Analysis**: Analyzes commits across all branches, filtering out those related solely to common open-source library integrations.
- **Developer Categorization**: Classifies contributors into full-time, part-time, and one-time contributors based on their commit frequency.
- **Repository Customization**: Supports analysis of multiple repositories as specified in the `aptos_repos.toml` configuration file. Replace this file with a .toml of any other list of repos you want to perform this analysis on. 

## Getting Started

1. **Clone the Repository**: Clone the `dev_metrics` repository to your local environment. You can do this by running the following command in your terminal:

    ```
    git clone https://github.com/zacharyr0th/dev_metrics.git
    ```

2. **Install Dependencies**: Install all required Python dependencies in the root directory of the project.

    ```
    pip install -r requirements.txt
    ```

3. **Set Up Your GitHub PAT**: Set up your Personal Access Token (PAT) for GitHub to fetch data. Follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for detailed instructions on how to create and manage a PAT.

4. **Configure `aptos_repos.toml`**: Add the repositories you wish to analyze to the `aptos_repos.toml` file, adhering to the TOML file format. The file structure should look like this:

    ```
    # Repositories
    [[repo]]
    url = "https://github.com/user/repo"

    [[repo]]
    url = "https://github.com/another_user/another_repo"
    ```

## Usage

Run the main script using `python3 main.py` in the project directory. The script performs the following tasks:
- Fetches data (`data_fetch.py`)
- Filters commits (`filter_commits.py`)
- Counts contributors (`count_contributors.py`)

Results will be displayed or saved based on the script's configuration.
