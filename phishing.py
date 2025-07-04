import re

def analyze_email(text):
    score = 0
    reasons = []

    # Normalize text
    text = text.lower()

    # Regex patterns for phishing detection
    patterns = {
        r"verify\s+.*account": 2,
        r"login\s+(now|immediately|urgently)": 2,
        r"click\s+(here|this\s+link)": 2,
        r"win\s+(money|cash|reward|gift)": 2,
        r"update\s+your\s+information": 2,
        r"unusual\s+activity\s+on\s+your\s+account": 3,
        r"your\s+account\s+has\s+been\s+(suspended|locked)": 3,
        r"http[s]?:\/\/(bit\.ly|tinyurl|shorturl|goo\.gl|t\.co)": 3,
        r"\d{4,}-\d{4,}-\d{4,}-\d{4,}": 3  # fake card numbers
    }

    for pattern, points in patterns.items():
        if re.search(pattern, text):
            score += points
            reasons.append(f"⚠️ Pattern matched: '{pattern}' (+{points})")

    # Extra bonus: count suspicious keywords
    keywords = ["urgent", "action required", "limited time", "password reset"]
    for kw in keywords:
        if kw in text:
            score += 1
            reasons.append(f"⚠️ Keyword detected: '{kw}' (+1)")

    # Final verdict
    if score >= 7:
        status = "🚨 Highly Suspicious Email!"
    elif score >= 4:
        status = "⚠️ Possible Phishing Detected"
    elif score > 0:
        status = "⚠️ Slightly Suspicious Content"
    else:
        status = "✅ Email seems clean."

    return status + "\n\n" + "\n".join(reasons)
