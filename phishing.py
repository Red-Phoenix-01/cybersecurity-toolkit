def analyze_email(text):
    keywords = ["verify your account", "login urgently", "click this link", "win money"]
    found = [kw for kw in keywords if kw in text.lower()]
    if found:
        return f"⚠️ Phishing phrases detected:\n- " + "\n- ".join(found)
    else:
        return "✅ Email seems clean."
