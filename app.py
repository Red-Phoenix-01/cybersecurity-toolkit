from flask import Flask, render_template, request, abort
from phishing import analyze_email
from url_scan import scan_url
from vuln_scan import scan_target
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tool = request.form.get('tool')
    data = request.form.get('data')
    ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 🔒 Shorten and sanitize the input data to avoid logging sensitive info
    safe_data = data[:100].replace('\n', ' ').replace('\r', '').strip()

    # 📝 Write to the log file
    log_line = f"[{timestamp}] IP: {ip} | Tool: {tool} | Data: {safe_data}\n"
    with open("usage_log.txt", "a") as logfile:
        logfile.write(log_line)

    if tool == 'phishing':
        return analyze_email(data)
    elif tool == 'url':
        return scan_url(data)
    elif tool == 'vuln':
        return scan_target(data)
    else:
        return "Invalid tool selected."

@app.route('/logs')
def view_logs():
    # Only allow local IPs for safety
    if request.remote_addr not in ['127.0.0.1', '::1']:
        return abort(403)  # Forbidden

    if os.path.exists("usage_log.txt"):
        with open("usage_log.txt", "r") as log:
            contents = log.read().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            return f"<pre>{contents}</pre>"
    else:
        return "No logs yet."


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)



