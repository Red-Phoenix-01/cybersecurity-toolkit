function analyze() {
  const tool = document.getElementById('tool').value;
  const data = document.getElementById('inputBox').value.trim();  // Removes spaces

  // ❌ Block analysis if input is empty
  if (!data) {
    alert("⚠️ Please enter something to analyze.");
    return;
  }

  // 🌐 Validation for vuln scanner
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
  const icon = document.querySelector('.toggle-icon');
  const currentBg = getComputedStyle(root).getPropertyValue('--bg-color').trim();

  // Animate only the emoji icon
  icon.classList.add('spin');
  setTimeout(() => icon.classList.remove('spin'), 600);

  if (currentBg === '#0f0f0f') {
    // Light theme
    root.style.setProperty('--bg-color', '#f5f7fa');
    root.style.setProperty('--text-color', '#222222');
    root.style.setProperty('--input-bg', '#ebeff3');
    root.style.setProperty('--result-bg', '#ffffff');
    root.style.setProperty('--textarea-text', '#222222');
    document.body.style.backgroundImage = "radial-gradient(circle at center, #f5f7fa, #dbe3ea)";
  } else {
    // Dark theme
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


function updatePlaceholder() {
  const tool = document.getElementById("tool").value;
  const inputBox = document.getElementById("inputBox");

  if (tool === "phishing") {
    inputBox.placeholder = "e.g. 'We detected unusual activity on your account. Click here to verify now.'";
  } else if (tool === "url") {
    inputBox.placeholder = "e.g. 'https://bit.ly/secure-login'";
  } else if (tool === "vuln") {
    inputBox.placeholder = "e.g. 'example.com' or '192.168.0.1'";
  } else {
    inputBox.placeholder = "Paste input here...";
  }
}

