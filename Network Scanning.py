import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set socket timeout to 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip}: Open")
        sock.close()
    except socket.error:
        pass  # Ignore socket errors (e.g., connection refused)

def scan_ip_range(ip_range, ports):
    for ip in range(1, 255):
        for port in ports:
            scan_port(f"{ip_range}.{ip}", port)

# Demo
if __name__ == "__main__":
    network_to_scan = "192.168.1"  # Replace with your network prefix
    common_ports = [21, 22, 80, 443]  # Example of common ports to scan

    print(f"Scanning network {network_to_scan}.0/24 for common ports...")
    for ip_range in range(1, 255):
        scan_ip_range(f"{network_to_scan}.{ip_range}", common_ports)