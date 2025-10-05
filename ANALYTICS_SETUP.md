# Google Analytics Setup Guide

This guide will help you complete the Google Analytics integration for your Jekyll blog.

## What's Already Configured

✅ **Privacy Policy Page**: Created at `/privacy-policy/`  
✅ **Cookie Consent Banner**: Interactive banner with settings modal  
✅ **Analytics Integration**: Google Analytics 4 (GA4) ready  
✅ **GDPR Compliance**: Cookie consent management  
✅ **Footer Link**: Privacy policy link added to footer  

## Setup Steps

### 1. Get Your Google Analytics Measurement ID

1. Go to [Google Analytics](https://analytics.google.com/)
2. Create a new GA4 property for your website
3. Copy your Measurement ID (format: `G-XXXXXXXXXX`)

### 2. Update Configuration

Edit `_config.yml` and replace the placeholder values:

```yaml
# Analytics
google_analytics: G-XXXXXXXXXX  # Replace with your actual GA4 measurement ID
google_site_verification: ABC123DEF456  # Optional: Google Search Console verification code
```

### 3. Test the Integration

1. Start your Jekyll server: `bundle exec jekyll serve`
2. Visit your site in a private/incognito browser window
3. You should see the cookie consent banner at the bottom
4. Accept cookies and check if analytics data appears in your GA4 dashboard

## Features Included

### Cookie Consent Banner
- **Accept All**: Enables all tracking
- **Decline**: Disables all non-essential tracking
- **Settings**: Granular control over cookie types
- **Persistent**: Remembers user choices for 365 days

### Privacy Policy
- **Comprehensive**: Covers data collection, usage, and rights
- **GDPR Compliant**: Includes required disclosures
- **Auto-updated**: Last updated date automatically generated
- **Accessible**: Linked from footer and cookie banner

### Analytics Configuration
- **Privacy-First**: Analytics disabled until user consent
- **Anonymized IP**: IP addresses are anonymized
- **No Ad Personalization**: Disabled by default
- **Consent Management**: Respects user cookie preferences

## Customization

### Cookie Banner Styling
Edit `_includes/cookie-consent.html` to customize:
- Colors and fonts
- Banner position and size
- Button styles
- Mobile responsiveness

### Privacy Policy Content
Edit `_pages/privacy-policy.md` to:
- Add your contact information
- Include specific data processing details
- Add additional legal requirements for your jurisdiction

### Analytics Settings
Edit `_includes/analytics.html` to:
- Add additional tracking codes
- Configure custom events
- Set up conversion tracking

## Verification

After setup, verify everything works:

1. **Cookie Banner**: Appears on first visit, disappears after consent
2. **Analytics**: Data appears in GA4 dashboard within 24-48 hours
3. **Privacy Policy**: Accessible via footer link and cookie banner
4. **Consent Management**: Analytics respects user choices

## Troubleshooting

### Analytics Not Working
- Check that your GA4 measurement ID is correct
- Verify the ID starts with "G-" (not "UA-")
- Ensure cookies are accepted
- Check browser console for errors

### Cookie Banner Not Appearing
- Clear browser cookies and refresh
- Check that `_includes/cookie-consent.html` exists
- Verify the include is added to your layout

### Privacy Policy Not Accessible
- Check that `_pages/privacy-policy.md` exists
- Verify the permalink is set to `/privacy-policy/`
- Ensure the page is included in your Jekyll build

## Legal Compliance

This setup provides a foundation for GDPR compliance, but you should:

1. **Review Privacy Policy**: Ensure it covers all your data processing activities
2. **Add Contact Information**: Include your actual contact details
3. **Legal Review**: Consider having a lawyer review your privacy policy
4. **Regular Updates**: Keep privacy policy current with your practices

## Support

For issues with this implementation:
1. Check the browser console for JavaScript errors
2. Verify all files are properly included
3. Test in different browsers and devices
4. Review Jekyll build logs for errors

---

*This setup provides a privacy-compliant foundation for analytics on your Jekyll blog.*