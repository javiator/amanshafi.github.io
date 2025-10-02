# Javiator's Blog

A personal blog built with Jekyll and the Minimal Mistakes theme, showcasing technical projects, tutorials, and insights.

## Features

- **Modern Design**: Clean, responsive layout using the Minimal Mistakes Jekyll theme
- **Content Management**: Easy-to-write Markdown posts with front matter
- **Navigation**: Top navigation with sample pages and author sidebar
- **Search**: Site-wide search functionality
- **Archives**: Organized content by year, category, and tag
- **Social Links**: Author sidebar with social media integration
- **SEO Optimized**: Built-in SEO tags and sitemap generation

## Local Development

### Prerequisites

- Docker and Docker Compose installed on your system

### Quick Start with Docker

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd javiator.github.io
   ```

2. **Start the development server**:
   ```bash
   docker compose up
   ```

3. **View your site**: Open [http://localhost:4000](http://localhost:4000) in your browser

4. **Stop the server**: Press `Ctrl+C` or run:
   ```bash
   docker compose down
   ```

### Docker Commands

- **Start in background**: `docker compose up -d`
- **View logs**: `docker compose logs -f`
- **Rebuild**: `docker compose up --build`
- **Stop**: `docker compose down`

   ```

## Content Management

### Creating New Posts

1. **Using the script** (recommended):
   ```bash
   python scripts/generate_post.py "Your Post Title"
   ```

2. **Manual creation**: Create a new file in `_posts/` with the format:
   ```
   YYYY-MM-DD-post-title.md
   ```

### Post Structure

Each post should include front matter at the top:
```yaml
---
title: "Your Post Title"
date: 2025-01-01
categories: [category1, category2]
tags: [tag1, tag2]
---
```

## Deployment

This blog is designed to work with GitHub Pages. Simply push your changes to the main branch and GitHub Pages will automatically build and deploy your site.

### GitHub Pages Configuration

- **Repository**: `javiator.github.io`
- **Branch**: `main` (or `gh-pages`)
- **Source**: Deploy from a branch
- **Theme**: Minimal Mistakes (configured in `_config.yml`)

## Project Structure

```
├── _config.yml          # Site configuration
├── _data/               # Data files (navigation, etc.)
├── _pages/              # Static pages (About, Projects, etc.)
├── _posts/              # Blog posts
├── assets/              # CSS, images, and other assets
├── scripts/             # Utility scripts
├── docker-compose.yml   # Docker development setup
└── README.md           # This file
```

---

## Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.
