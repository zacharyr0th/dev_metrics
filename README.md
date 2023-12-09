# `dev_metrics` Project README

## Introduction

`dev_metrics` is a versatile analysis tool designed for evaluating development activities across various repositories. This directory contains aptos_repos.toml which has a list of repositories who are dependent on Aptos-Core, the source code for the Aptos blockchain.

## Methodology

### Commit Counting

- **Branches:** Accounts for commits from all branches.
- **Open Source Libraries:** Omits commits related solely to the integration of common libraries from the activity metrics.

### Developer Classification

- **Developers:** Targets original code authors, including those actively contributing to the codebase.
- **Full-Time Contributors:** Designated as contributors with code commits on 10 or more days within a month.
- **Part-Time Contributors:** Identified as contributors with fewer than 10 days of code commits in a month.
- **One-Time Contributors:** Recognizes contributors with a single code commit in a three-month period.

## Getting Started

1. **Clone the repository**: Download the `dev_metrics` codebase to your local machine.
2. **Install Dependencies**: Ensure all required dependencies are installed.
3. **Configure Your TOML File**: `dev_metrics` can analyze any repository listed in a TOML configuration file. Format your file like this:

   ```toml
   [[repo]]
   url = "https://github.com/example/blockchain-core"

   [[repo]]
   url = "https://github.com/anotherexample/project"

## Usage
- Execute the tool using `python3 dev_metrics.py` from the directory.
- View the following results in the generated CSV report:
  - **Developers**
  - **Full-Time Contributors**
  - **Part-Time Contributors**
  - **One-Time Contributors**

## Contribution
Contributions are welcome. Please adhere to these guidelines:
- Fork the repository.
- Create a new feature branch.
- Commit your changes.
- Submit a detailed pull request.
