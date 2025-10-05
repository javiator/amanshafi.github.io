# Cookie Consent Test Guide

This guide helps you verify that the cookie consent banner is working on all pages and layouts.

## Test Steps

### 1. Clear Browser Data
- Open browser developer tools (F12)
- Go to Application/Storage tab
- Clear all cookies for your domain
- Refresh the page

### 2. Test Each Page Type

Visit each of these pages and verify the cookie consent banner appears:

#### Single Layout Pages
- **Home Page**: `/` (index.md)
- **About Page**: `/about/` 
- **Projects Page**: `/projects/`
- **Privacy Policy**: `/privacy-policy/`

#### Archive Layout Pages  
- **Posts Archive**: `/posts/` (posts layout)
- **Tags Archive**: `/tags/` (tags layout)  
- **Categories Archive**: `/categories/` (categories layout)

### 3. Test Cookie Functionality

On each page:
1. **Accept All** - Banner should disappear
2. **Refresh page** - Banner should NOT reappear
3. **Clear cookies** - Banner should reappear

### 4. Test Custom Settings

1. **Click Settings** in cookie banner
2. **Uncheck Analytics** and **Preferences** (keep only Essential)
3. **Click Save Settings** - Banner should disappear
4. **Refresh page** - Banner should NOT reappear

## Debug Commands

Open browser console (F12) and run these commands:

```javascript
// Check if cookie consent elements exist
document.getElementById('cookie-consent-banner') ? '✅ Banner found' : '❌ Banner missing'

// Check current cookie status
debugCookies()

// Clear all cookies for testing
clearCookieConsent()

// Test custom settings scenario
testCustomSettings()
```

## Expected Results

✅ **All pages should show cookie banner on first visit**  
✅ **Banner should disappear after accepting/declining**  
✅ **Banner should stay hidden on page refresh**  
✅ **Custom settings should work correctly**  
✅ **Analytics should respect user choices**

## Troubleshooting

### Banner Not Appearing
- Check browser console for JavaScript errors
- Verify `_includes/cookie-consent.html` exists
- Check that `body` section in `_config.yml` includes the cookie consent

### Banner Keeps Reappearing
- Check cookie values in browser dev tools
- Run `debugCookies()` in console
- Verify `hasConsent()` function logic

### Analytics Not Working
- Check Google Analytics measurement ID in `_config.yml`
- Verify analytics consent is set to 'true'
- Check browser network tab for GA requests

---

*This test ensures cookie consent works across all page layouts and user scenarios.*