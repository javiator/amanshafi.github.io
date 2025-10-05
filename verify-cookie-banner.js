// Cookie Banner Verification Script
// Run this in browser console to check if cookie banner is working

console.log("🍪 Cookie Banner Verification Script");
console.log("=====================================");

// Check if cookie banner elements exist
const banner = document.getElementById('cookie-consent-banner');
const modal = document.getElementById('cookie-settings-modal');
const acceptBtn = document.getElementById('cookie-accept');
const declineBtn = document.getElementById('cookie-decline');
const settingsBtn = document.getElementById('cookie-settings');

console.log("📋 Element Check:");
console.log("Banner element:", banner ? "✅ Found" : "❌ Missing");
console.log("Modal element:", modal ? "✅ Found" : "❌ Missing");
console.log("Accept button:", acceptBtn ? "✅ Found" : "❌ Missing");
console.log("Decline button:", declineBtn ? "✅ Found" : "❌ Missing");
console.log("Settings button:", settingsBtn ? "✅ Found" : "❌ Missing");

// Check if debug functions are available
console.log("\n🔧 Function Check:");
console.log("debugCookies:", typeof window.debugCookies);
console.log("clearCookieConsent:", typeof window.clearCookieConsent);
console.log("testCustomSettings:", typeof window.testCustomSettings);

// Check cookie status
console.log("\n🍪 Cookie Status:");
console.log("cookie-consent:", document.cookie.split(';').find(c => c.includes('cookie-consent')));
console.log("analytics-cookies:", document.cookie.split(';').find(c => c.includes('analytics-cookies')));
console.log("preference-cookies:", document.cookie.split(';').find(c => c.includes('preference-cookies')));

// Check if banner is visible
if (banner) {
    const isVisible = banner.style.display !== 'none' && banner.offsetParent !== null;
    console.log("\n👁️ Visibility Check:");
    console.log("Banner visible:", isVisible ? "✅ Yes" : "❌ No");
    console.log("Banner display style:", banner.style.display);
    console.log("Banner computed style:", window.getComputedStyle(banner).display);
}

// Check for any console errors
console.log("\n🚨 Error Check:");
console.log("Check browser console for any JavaScript errors");

// Recommendations
console.log("\n💡 Recommendations:");
if (!banner) {
    console.log("❌ Cookie banner not found - check if _includes/cookie-consent.html is being loaded");
} else if (!window.debugCookies) {
    console.log("❌ Debug functions not available - check if JavaScript is loading properly");
} else {
    console.log("✅ Cookie banner appears to be set up correctly");
    console.log("Try running debugCookies() to see detailed cookie status");
}