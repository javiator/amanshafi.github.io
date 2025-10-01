#!/usr/bin/env python3
"""
Generate a Jekyll blog post from external repository information.
"""

import os
import re
import sys
import requests
from datetime import datetime
from urllib.parse import quote
import json

def fetch_readme_content(repo, ref, module_path, token=None):
    """Fetch README content from GitHub repository."""
    # Determine README path
    readme_path = f"{module_path}/README.md" if module_path else "README.md"
    
    # Try to get default branch if ref not provided
    if not ref:
        headers = {}
        if token:
            headers["Authorization"] = f"token {token}"
        
        try:
            response = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
            if response.status_code == 200:
                ref = response.json().get("default_branch", "main")
            else:
                ref = "main"
        except:
            ref = "main"
    
    # Try raw.githubusercontent.com first (works for public repos)
    raw_url = f"https://raw.githubusercontent.com/{repo}/{ref}/{readme_path}"
    
    try:
        response = requests.get(raw_url)
        if response.status_code == 200:
            return response.text
    except:
        pass
    
    # Fallback to GitHub API (requires token for private repos)
    if token:
        api_url = f"https://api.github.com/repos/{repo}/contents/{readme_path}"
        headers = {"Authorization": f"token {token}"}
        if ref:
            api_url += f"?ref={ref}"
        
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                content = response.json().get("content", "")
                import base64
                return base64.b64decode(content).decode('utf-8')
        except:
            pass
    
    return None

def extract_functional_overview(readme_content):
    """Extract functional overview from README content."""
    if not readme_content:
        return ""
    
    lines = readme_content.split('\n')
    overview_sections = []
    in_overview = False
    current_section = []
    
    # Look for overview sections
    for i, line in enumerate(lines):
        line_lower = line.lower().strip()
        
        # Check if this is an overview section header
        if any(keyword in line_lower for keyword in ['# overview', '# what is', '# features', '# about']):
            in_overview = True
            current_section = [line]
            continue
        
        # Check if we hit a section we want to exclude
        if any(keyword in line_lower for keyword in ['# installation', '# setup', '# usage', '# examples', '# benchmarks', '# getting started']):
            if in_overview and current_section:
                overview_sections.extend(current_section)
            in_overview = False
            current_section = []
            continue
        
        # If we're in an overview section, collect content
        if in_overview:
            # Stop at next major section (## or ###)
            if line.startswith('#') and not line.startswith('##'):
                if current_section:
                    overview_sections.extend(current_section)
                break
            
            # Skip badges and empty lines at start
            if not current_section and (line.strip() == '' or 'badge' in line_lower or '![[' in line):
                continue
            
            current_section.append(line)
            
            # Stop after 3 paragraphs or 10 lines
            if len(current_section) > 10:
                break
    
    # If no specific overview section found, try to get first few paragraphs
    if not overview_sections:
        current_section = []
        for line in lines:
            if line.strip() == '':
                if current_section:
                    overview_sections.extend(current_section)
                    break
                continue
            
            # Skip badges
            if 'badge' in line.lower() or '![[' in line:
                continue
            
            current_section.append(line)
            if len(current_section) > 8:  # Limit to first 8 lines
                break
    
    # Clean up and return
    overview_text = '\n'.join(overview_sections).strip()
    
    # Remove excessive whitespace
    overview_text = re.sub(r'\n\s*\n\s*\n', '\n\n', overview_text)
    
    return overview_text

def generate_slug(title):
    """Generate a URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

def generate_auto_summary(title, overview):
    """Generate auto summary from title and overview."""
    if overview:
        # Get first sentence from overview
        sentences = re.split(r'[.!?]+', overview)
        first_sentence = sentences[0].strip() if sentences else ""
        
        if first_sentence and len(first_sentence) > 10:
            summary = f"{title}: {first_sentence}"
        else:
            summary = f"Overview and key learnings for {title}"
    else:
        summary = f"Overview and key learnings for {title}"
    
    # Truncate to ~160 characters
    if len(summary) > 160:
        summary = summary[:157] + "..."
    
    return summary

def main():
    # Get environment variables
    source_repo = os.getenv('SOURCE_REPO')
    ref = os.getenv('REF')
    module_path = os.getenv('MODULE_PATH', '')
    post_title = os.getenv('POST_TITLE')
    post_date = os.getenv('POST_DATE')
    categories = os.getenv('CATEGORIES', '')
    tags = os.getenv('TAGS', '')
    extra_content = os.getenv('EXTRA_CONTENT', '')
    custom_summary = os.getenv('CUSTOM_SUMMARY', '')
    dry_run = os.getenv('DRY_RUN', 'true').lower() == 'true'
    token = os.getenv('SOURCE_REPOS_TOKEN')
    
    # Validate required inputs
    if not source_repo or not post_title:
        print("Error: source_repo and post_title are required")
        sys.exit(1)
    
    # Set default date
    if not post_date:
        post_date = datetime.now().strftime('%Y-%m-%d')
    
    # Fetch README content
    print(f"Fetching README from {source_repo}...")
    readme_content = fetch_readme_content(source_repo, ref, module_path, token)
    
    # Extract functional overview
    overview = extract_functional_overview(readme_content)
    
    # Generate summary
    if custom_summary:
        summary = custom_summary
    else:
        summary = generate_auto_summary(post_title, overview)
    
    # Format categories and tags
    categories_list = [cat.strip() for cat in categories.split(',') if cat.strip()] if categories else []
    tags_list = [tag.strip() for tag in tags.split(',') if tag.strip()] if tags else []
    
    # Generate post content
    post_content = f"""---
title: "{post_title}"
date: {post_date}
categories: {json.dumps(categories_list)}
tags: {json.dumps(tags_list)}
description: "{summary}"
toc: true
last_modified_at: {post_date}
---

### Overview
{overview if overview else "No overview available."}

### Key learnings / knowledge share
{extra_content if extra_content else "No additional content provided."}

### Links
- Repository: https://github.com/{source_repo}
- Path: https://github.com/{source_repo}/tree/{ref or 'main'}/{module_path if module_path else ''}
- README: https://github.com/{source_repo}/blob/{ref or 'main'}/{module_path + '/README.md' if module_path else 'README.md'}
"""
    
    # Write to file
    with open('generated_post.md', 'w', encoding='utf-8') as f:
        f.write(post_content)
    
    print("Post generated successfully!")
    if dry_run:
        print("Dry run mode - post saved as generated_post.md")
    else:
        print("Post will be committed to repository")

if __name__ == "__main__":
    main()
