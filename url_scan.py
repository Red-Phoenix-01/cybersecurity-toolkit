import re

def scan_url(url):
    suspicious = ["bit.ly", "tinyurl", "free", "login", "secure", "verify"]
    found = [s for s in suspicious if s in url.lower()]
    if found:
        return f"⚠️ Suspicious patterns in URL:\n- " + "\n- ".join(found)
    elif not re.match(r"^https?://", url):
        return "⚠️ Invalid URL format."
    else:
        return "✅ URL appears safe."
