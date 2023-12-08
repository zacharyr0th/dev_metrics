# `dev_metrics` Project README

## Introduction

`dev_metrics` is a specialized tool for analyzing development activities across multiple repositories, as defined in `aptosRepos.toml`. It provides valuable insights into both the quantity and quality of contributions, enhancing the understanding of software development dynamics.

## Methodology

### Commit Counting

- **Branches:** Includes commits from all branches.
- **Open Source Libraries:** Excludes commits related to the integration of common libraries from code activity metrics.

### Developer Classification

- **Developers:** Focuses on original code authors, including active codebase contributors who merge pull requests.
- **Full-Time Contributors:** Contributors with code commits on 10 or more days in a month.
- **Part-Time Contributors:** Contributors with fewer than 10 days of code commits in a month.
- **One-Time Contributors:** Contributors with a single code commit in a rolling 3-month period.

## Getting Started

1. Clone the repository.
2. Install necessary dependencies.
3. Place your `aptosRepos.toml` in the root directory.
4. Execute the tool following the provided instructions.

## Usage

- Execute the tool by running `python3 dev_metrics.py` from the dev_metrics directory.
- The results will be categorized as per the outlined methodologies and can be viewed in the generated csv report.
- **Configuration:** Keep `aptosRepos.toml` updated with current repositories that are dependent on [Aptos-Core]([url](https://github.com/aptos-labs/aptos-core)).
- **Data Interpretation:** Use project-specific knowledge for more accurate insights from the data.

## Contribution

Contributions to `dev_metrics` are encouraged. Please follow these steps:

- Fork the repository.
- Create a feature branch.
- Commit your changes.
- Submit a pull request with a clear enhancement or fix description.

## License

This project is licensed under the Apache License 2.0, a permissive open-source license. This license explicitly grants patent rights from contributors to users and protects against trademark abuse. It allows considerable freedom in the use, modification, and distribution of the software, even for proprietary purposes, and requires modifications to be stated. 

For full terms and conditions, see the [LICENSE](LICENSE) file.
