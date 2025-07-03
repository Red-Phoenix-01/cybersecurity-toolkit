from flask import Flask, render_template, request
from phishing import analyze_email
from url_scan import scan_url
from vuln_scan import scan_target

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tool = request.form.get('tool')
    data = request.form.get('data')

    if tool == 'phishing':
        return analyze_email(data)
    elif tool == 'url':
        return scan_url(data)
    elif tool == 'vuln':
        return scan_target(data)
    else:
        return "Invalid tool selected."

if __name__ == '__main__':
    app.run(debug=True)
