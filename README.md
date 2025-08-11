# 🛡️ Cybersecurity Toolkit 🔐

A voice-enhanced, dark-mode-friendly web app built with **Flask** for analyzing:

- 📩 Phishing Emails  
- 🌐 Suspicious URLs  
- 🛠️ Basic Vulnerability Port Scans  

Built with ❤️ using Python, Flak, HTML, CSS, and JavaScript.

---

## 🔍 Preview

![Cybersecurity Toolkit Screenshot](screenshot.png)

---

## 🚀 Live Demo

[🔗 Try the app](https://redphoenix01.pythonanywhere.com)

✅ Always-on  
💬Voice-Enabled
🚄 Built with Flask + JS + Cyber 🛡️



## 🚀 Features

- ⚡ Clean, responsive UI with light/dark mode toggle  
- 🔊 **Voice greetings and alerts** using Web Speech API 
- 🔐 Detects phishing content, suspicious URLs, and open ports 
- 🎯 Minimal setup, perfect for demos, portfolios, or security labs 
- 💡 Lightweight setup — perfect for demos, portfolios, or quick threat analysis 
- 🧪 Built for hands-on cybersecurity awareness

---

## 🗂️ Project Structure

```
Cybersecurity-Toolkit/
├── app.py               # Main Flask app
├── phishing.py          # Phishing detection logic
├── url_scan.py          # URL scanning logic
├── vuln_scan.py         # Port scanner
├── requirements.txt     # Python dependencies
│
├── templates/
│   └── index.html       # Frontend HTML
│
└── static/
    ├── css/
    │   └── style.css    # Styles
    └── js/
        └── script.js    # JavaScript (theme, voice, fetch)
```



---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python + Flask 
- **Deployment**: Railway
- **Voice Feature**: Web Speech API (JS)

---

## 🧠 Modules

- `phishing.py`: Detects high-risk phrases used in phishing attempts  
- `url_scan.py`: Scans URLs using **heuristics + VirusTotal API**  
- `vuln_scan.py`: Scans for common exposed ports on target IP/domains  
- `script.js`: Controls UI, fetch calls, voice feedback, and animations   

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 2. Navigate into the folder
cd YOUR_REPO_NAME

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py






Visit http://localhost:5000 in your browser.



