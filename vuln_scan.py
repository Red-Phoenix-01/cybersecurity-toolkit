import socket

def scan_target(target):
    ports = [21, 22, 23, 80, 443, 8080]
    open_ports = []
    try:
        # Reject overly long or invalid inputs
        if len(target) > 100 or not target.replace(".", "").isalnum():
            return "❌ Invalid input: Please enter a valid IP address or domain."

        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return "❌ Error: Could not resolve the host. Make sure it's a valid domain/IP."
    except UnicodeEncodeError:
        return "❌ Unicode Error: Your input contains invalid characters or is too long."

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except Exception as e:
            return f"❌ Error scanning port {port}: {e}"

    if open_ports:
        return f"⚠️ Open Ports Detected on {target}:\n- " + "\n- ".join(map(str, open_ports))
    else:
        return f"✅ No common open ports found on {target}."
