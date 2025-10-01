# Blog Post Generator

This script generates Jekyll blog posts from external GitHub repositories.

## Usage

The script is used by the GitHub Actions workflow `publish-external-update.yml`. To use it:

1. Go to your repository's Actions tab
2. Select "Publish External Update" workflow
3. Click "Run workflow"
4. Fill in the required fields:
   - **Source repository**: The GitHub repo to read from (e.g., `javiator/learn-ai`)
   - **Post title**: The title for your blog post
   - **Categories/Tags**: Optional comma-separated lists
   - **Extra content**: Optional markdown content for learnings/knowledge share
   - **Dry run**: Set to true to preview the generated post

## Features

- Fetches README content from any GitHub repository
- Extracts functional overview (excludes installation/usage sections)
- Auto-generates summary from title and overview
- Creates properly formatted Jekyll post with front matter
- Supports both public and private repositories (with token)

## Private Repository Access

For private repositories, add a `SOURCE_REPOS_TOKEN` secret to your repository with appropriate permissions.
