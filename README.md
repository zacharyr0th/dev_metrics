# `dev_metrics` Project README

## Introduction

`dev_metrics` is a comprehensive tool designed for analyzing development activities within various repositories, particularly those related to the Aptos blockchain. It includes scripts for data fetching, filtering commits, and counting contributors, making it a powerful resource for developers and project managers.

## Features

- **Commit Analysis**: Analyzes commits across all branches, filtering out those related solely to common open-source library integrations.
- **Developer Categorization**: Classifies contributors into full-time, part-time, and one-time contributors based on their commit frequency.
- **Repository Customization**: Supports analysis of multiple repositories as specified in the `aptosRepos.toml` configuration file.

## Getting Started

1. **Clone the Repository**: Download the `dev_metrics` codebase to your local environment.
2. **Install Dependencies**: Ensure all required Python dependencies are installed for the project.
3. **Configure `aptosRepos.toml`**: Add the repositories you wish to analyze in the TOML file format:

   ```toml
   [[repo]]
   url = "https://github.com/example/blockchain-core"

   [[repo]]
   url = "https://github.com/anotherexample/project"

## Usage

Run the main script using `python3 main.py` in the project directory. The script performs the following tasks:
- Fetches data (`data_fetch.py`)
- Filters commits (`filter_commits.py`)
- Counts contributors (`count_contributors.py`)
Results will be displayed or saved based on the script's configuration.

## Contribution

Your contributions can help improve `dev_metrics`. Please follow these steps to contribute:
- Fork the repository.
- Create a new branch for your feature.
- Make your changes and commit them.
- Open a pull request with a detailed description of your changes.
