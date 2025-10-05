# Cloudflare Web Analytics

## Setup

Add your token to `_config.yml`:
```yaml
analytics:
  provider: "cloudflare"
  cloudflare:
    token: "YOUR_TOKEN_HERE"
```

Restart Jekyll after config changes: `docker compose restart`

## Implementation

- `_includes/head/custom.html` - Loads beacon script when configured
- Automatically included on all pages via Minimal Mistakes theme

## Coverage

All page types: home, posts, pages, archives (tags, categories)

## Notes

CORS errors on localhost are expected - works on production.

