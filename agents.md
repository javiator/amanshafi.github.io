# AI Agent Guidelines for Javiator's Blog

This document provides a high-level overview for AI agents working with this blog project. For detailed implementation guidelines, refer to the Cursor rules in `.cursor/rules/`.

## Project Overview

This is a Jekyll-based blog showcasing **"Tenant Management: An Evolutionary Project"** - a systematic approach to architectural evolution through 5 different technology stacks and architectural approaches.

## Cursor Rules Structure

This project uses the modern Cursor rules format with `.cursor/rules/` directory containing `.mdc` files:

- **`.cursor/rules/evolutionary-project-framework.mdc`**: Core framework and project context
- **`.cursor/rules/content-creation.mdc`**: Content creation guidelines and processes  
- **`.cursor/rules/technical-standards.mdc`**: Technical standards and implementation details

## Quick Reference

### Evolution Structure
```
Evolution 1: Single-File Foundation (✅ Complete)
Evolution 2: Modular Architecture (✅ Complete)  
Evolution 3: Java Enterprise Stack (🔄 Active)
Evolution 4: AI-Enhanced Interface (📋 Planned)
Evolution 5: Conversational Interface (📋 Planned)
```

### Current Status
- **Total Posts**: 7 (5 evolutionary + 2 supporting)
- **Active Evolutions**: 3 (1, 2, 3)
- **Technologies**: Python, Flask, Java, Spring Boot, React, Docker

### Key Principles
1. **Progressive Complexity**: Each evolution builds upon previous learnings
2. **Technology Mastery**: Deep dive into different technology stacks
3. **Architectural Patterns**: From simple to enterprise-ready architectures
4. **Decision Making**: Documented reasoning behind each architectural choice
5. **Portfolio Value**: Comprehensive case study in software evolution

## Essential Guidelines

### Post Creation
- **Assign to Evolution**: Determine which evolution the post belongs to
- **Add Evolution Metadata**: Include the 5 evolution fields in frontmatter
- **Include Navigation Components**: Add project tags, post navigation, and evolution posts
- **Use Mermaid Diagrams**: Illustrate architectural concepts

### Post Structure Template
```markdown
# Post Title

{% include evolution/post-navigation.html %}

## Post Content...

{% include evolution/evolution-posts.html %}

## Key Learnings
```

### Required Metadata
```yaml
# Evolutionary Project Fields (REQUIRED)
project: "Tenant Management"
project_type: "evolutionary"
evolution: "Evolution X: [Name]"
evolution_number: X
evolution_focus: "[Focus Area]"
```

## Navigation Components

- **Post Navigation**: `{% include evolution/post-navigation.html %}` - Evolution context and navigation (includes project branding)
- **Evolution Posts**: `{% include evolution/evolution-posts.html %}` - Related posts in same evolution

## Success Criteria

### For New Content
- ✅ Properly assigned to evolution
- ✅ Includes evolution metadata
- ✅ Has appropriate navigation links
- ✅ Uses Mermaid diagrams where relevant
- ✅ Maintains learning journey narrative

### For Updates
- ✅ Preserves evolution context
- ✅ Updates navigation components
- ✅ Keeps diagrams current
- ✅ Maintains systematic progression

## Detailed Guidelines

For comprehensive implementation details, refer to:
- **Framework Details**: `.cursor/rules/evolutionary-project-framework.mdc`
- **Content Creation**: `.cursor/rules/content-creation.mdc`
- **Technical Standards**: `.cursor/rules/technical-standards.mdc`

---

*This framework represents a learning-first approach to software development, where each evolution serves both practical and educational purposes.*