import os
import requests

# Read content from results.txt
file_path = 'results.txt'

with open(file_path, 'r') as file:
    content = file.read()

# Check if there is content in the file
if content:
    # Format content using Markdown
    markdown_content = f"## PSScriptAnalyzer Results\n\n```\n{content}\n```"

    # Get GitHub repository and pull request information from environment variables
    repository = os.getenv('GITHUB_REPOSITORY')
    pull_request_number = os.getenv('GITHUB_PULL_REQUEST_NUMBER')

    # Get GitHub token from environment variable
    github_token = os.getenv('GITHUB_TOKEN')

    # Post a comment to the pull request with the formatted content
    comment_url = f'https://api.github.com/repos/{repository}/issues/{pull_request_number}/comments'
    headers = {'Authorization': f'Bearer {github_token}'}
    payload = {'body': markdown_content}
    
    response = requests.post(comment_url, headers=headers, json=payload)

    if response.status_code == 201:
        print('Comment posted successfully.')
    else:
        print(f'Failed to post comment. Status code: {response.status_code}')
else:
    print('No linting errors found. All good!')
