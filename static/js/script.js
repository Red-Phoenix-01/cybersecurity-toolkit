function analyze() {
  const tool = document.getElementById('tool').value;
  const data = document.getElementById('inputBox').value;

  // 🌐 Extra validation for vuln scanner
  if (tool === "vuln" && data.length > 100) {
    alert("⚠️ The domain or IP is too long. Please enter a valid host like 'example.com' or '127.0.0.1'.");
    return;
  }

  // Show loading spinner
  document.getElementById('loading').style.display = "block";
  const resultBox = document.getElementById('resultBox');
  resultBox.style.opacity = 0;

  fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: `tool=${tool}&data=${encodeURIComponent(data)}`
  })
    .then(res => res.text())
    .then(result => {
      document.getElementById('loading').style.display = "none";

      resultBox.innerText = result;
      resultBox.style.animation = 'none';
      void resultBox.offsetWidth;
      resultBox.style.animation = 'fadeIn 0.5s ease forwards';

      // Voice alert
      if (result.includes("⚠️") || result.includes("❌")) {
        speakResult("Warning: Suspicious result detected.");
      } else if (result.includes("✅")) {
        speakResult("Result looks safe.");
      }
    });
}

function speakResult(text) {
  if ('speechSynthesis' in window) {
    const utter = new SpeechSynthesisUtterance(text);
    utter.rate = 1;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utter);
  }
}

function toggleTheme() {
  const root = document.documentElement;
  const currentBg = getComputedStyle(root).getPropertyValue('--bg-color').trim();

  if (currentBg === '#0f0f0f') {
    // Switch to light theme
    root.style.setProperty('--bg-color', '#e0f2ff');
    root.style.setProperty('--text-color', '#0f0f0f');
    root.style.setProperty('--input-bg', '#f0f0f0');
    root.style.setProperty('--result-bg', '#ffffff');
    root.style.setProperty('--textarea-text', '#000000');
    document.body.style.backgroundImage = "radial-gradient(circle at center, #e0f2ff, #cce7f5)";
  } else {
    // Switch back to dark theme
    root.style.setProperty('--bg-color', '#0f0f0f');
    root.style.setProperty('--text-color', '#f2f2f2');
    root.style.setProperty('--input-bg', '#1a1a1a');
    root.style.setProperty('--result-bg', '#1e1e1e');
    root.style.setProperty('--textarea-text', '#ffffff');
    document.body.style.backgroundImage = "radial-gradient(circle at center, #0f0f0f 0%, #050505 100%)";
  }
}

// ✅ Voice greeting on page load based on time
window.onload = function () {
  const hour = new Date().getHours();
  let timeGreeting = "Hello";

  if (hour < 12) {
    timeGreeting = "Good morning";
  } else if (hour < 18) {
    timeGreeting = "Good afternoon";
  } else {
    timeGreeting = "Good evening";
  }

  speakResult(`${timeGreeting}, welcome to the Cybersecurity Toolkit. Let's get started.`);
};
