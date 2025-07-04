import re
import requests
from urllib.parse import urlparse, unquote

def check_with_virustotal(url):
    api_key = "6d4bcdf39430ccf53470b4525dc9e35cbe122d51ff8f30be67d114a4867475e0"  # 🔑 Replace this with your VirusTotal public API key
    headers = {"x-apikey": api_key}
    vt_url = "https://www.virustotal.com/api/v3/urls"

    try:
        response = requests.post(vt_url, headers=headers, data={"url": url})
        if response.status_code != 200:
            return "⚠️ VirusTotal: API request failed or limit reached."

        scan_id = response.json()["data"]["id"]
        result = requests.get(f"{vt_url}/{scan_id}", headers=headers)
        data = result.json()["data"]

        verdicts = data["attributes"]["last_analysis_stats"]
        malicious = verdicts.get("malicious", 0)
        suspicious = verdicts.get("suspicious", 0)

        if malicious > 0 or suspicious > 0:
            reasons = [k for k, v in verdicts.items() if v > 0]
            return f"🚨 VirusTotal flagged this as {', '.join(reasons)} by {malicious + suspicious} engine(s)."
        else:
            return "✅ VirusTotal: No engines flagged this URL."

    except Exception as e:
        return f"⚠️ Error querying VirusTotal: {e}"

def scan_url(url):
    suspicious_keywords = [
        "bit.ly", "tinyurl", "free", "login", "secure", "verify",
        "account", "update", "bank", "win", "confirm"
    ]
    suspicious_tlds = ['.xyz', '.top', '.gq', '.tk', '.ml', '.cf', '.icu', '.buzz']
    known_brands = ["google", "facebook", "amazon", "paypal", "microsoft"]
    flagged_items = []

    # ✅ Check URL format
    if not re.match(r"^https?://[a-zA-Z0-9\-\.]+\.[a-z]{2,}", url):
        return "❌ Invalid URL format."

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    full_path = parsed.path + parsed.query
    decoded_url = unquote(url)

    # ✅ Keyword detection
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            flagged_items.append(f"⚠️ Keyword '{keyword}' found in URL")

    # ✅ Suspicious TLD
    if any(domain.endswith(tld) for tld in suspicious_tlds):
        flagged_items.append("⚠️ Suspicious top-level domain (TLD) used")

    # ✅ Fake login impersonation
    if re.search(r"(login|secure)[\.-](paypal|facebook|google|amazon)", domain):
        flagged_items.append("⚠️ Domain mimics a known service (e.g., PayPal, Google)")

    # ✅ Unusual ports
    if ":" in domain and not domain.endswith(":80") and not domain.endswith(":443"):
        flagged_items.append("⚠️ Unusual port used in URL")

    # ✅ Base64-like patterns
    if re.search(r"([A-Za-z0-9+/]{10,}={0,2})", decoded_url):
        flagged_items.append("⚠️ Encoded (Base64-like) data found in URL")

    # ✅ Typosquatting patterns
    for brand in known_brands:
        if re.search(rf"{brand[0]}[^a-zA-Z0-9]*{brand[1:]}", domain) and brand not in domain:
            flagged_items.append(f"⚠️ Domain may be typosquatting '{brand}'")

    # ✅ Construct report
    if flagged_items:
        report = "🚨 Suspicious URL Detected:\n- " + "\n- ".join(flagged_items)
    else:
        report = "✅ No major local red flags detected."

    # ✅ Simulated behavior analysis
    if "https://" not in url:
        report += "\n⚠️ This URL is not using HTTPS — it may not be secure."
    if "login" in url and "https" not in url:
        report += "\n🔒 Login-related URL without HTTPS — high risk."
    if "?" not in url:
        report += "\n🔍 No query parameters found — may look clean but could redirect."
    if len(url) < 30:
        report += "\n🧩 Very short URL — may be hiding its true destination."

    # ✅ Add VirusTotal verdict
    report += "\n\n" + check_with_virustotal(url)
    return report
