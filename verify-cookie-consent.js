// Cookie Consent Verification Script
// Run this in browser console to verify cookie consent is working

(function() {
  'use strict';
  
  console.log('🍪 Cookie Consent Verification Script');
  console.log('=====================================');
  
  // Check if cookie consent elements exist
  const banner = document.getElementById('cookie-consent-banner');
  const modal = document.getElementById('cookie-settings-modal');
  const acceptBtn = document.getElementById('cookie-accept');
  const declineBtn = document.getElementById('cookie-decline');
  const settingsBtn = document.getElementById('cookie-settings');
  
  console.log('Element Check:');
  console.log('✅ Banner:', banner ? 'Found' : '❌ Missing');
  console.log('✅ Modal:', modal ? 'Found' : '❌ Missing');
  console.log('✅ Accept Button:', acceptBtn ? 'Found' : '❌ Missing');
  console.log('✅ Decline Button:', declineBtn ? 'Found' : '❌ Missing');
  console.log('✅ Settings Button:', settingsBtn ? 'Found' : '❌ Missing');
  
  // Check cookie values
  function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }
  
  const consent = getCookie('cookie-consent');
  const analytics = getCookie('analytics-cookies');
  const preferences = getCookie('preference-cookies');
  
  console.log('\nCookie Status:');
  console.log('Consent:', consent || 'Not set');
  console.log('Analytics:', analytics || 'Not set');
  console.log('Preferences:', preferences || 'Not set');
  
  // Check banner visibility
  const bannerVisible = banner && banner.style.display !== 'none';
  console.log('\nBanner Status:');
  console.log('Visible:', bannerVisible ? 'Yes' : 'No');
  
  // Check if gtag is available
  const gtagAvailable = typeof window.gtag !== 'undefined';
  console.log('\nAnalytics Status:');
  console.log('Google Analytics (gtag):', gtagAvailable ? 'Available' : 'Not available');
  
  // Overall status
  const allElementsPresent = banner && modal && acceptBtn && declineBtn && settingsBtn;
  const hasConsent = consent === 'accepted' || consent === 'custom' || consent === 'declined';
  
  console.log('\nOverall Status:');
  console.log(allElementsPresent ? '✅ All elements present' : '❌ Some elements missing');
  console.log(hasConsent ? '✅ Consent recorded' : '❌ No consent recorded');
  console.log(bannerVisible ? '⚠️  Banner is visible (expected if no consent)' : '✅ Banner hidden (expected if consent given)');
  
  // Recommendations
  console.log('\nRecommendations:');
  if (!allElementsPresent) {
    console.log('❌ Fix: Ensure cookie-consent.html is included on this page');
  }
  if (!hasConsent && !bannerVisible) {
    console.log('❌ Fix: Banner should be visible when no consent is given');
  }
  if (hasConsent && bannerVisible) {
    console.log('❌ Fix: Banner should be hidden when consent is given');
  }
  if (allElementsPresent && hasConsent && !bannerVisible) {
    console.log('✅ Everything looks good!');
  }
  
  console.log('\nTest Commands:');
  console.log('clearCookieConsent() - Clear all cookies and reload');
  console.log('testCustomSettings() - Test custom settings scenario');
  console.log('debugCookies() - Show detailed cookie information');
  
})();