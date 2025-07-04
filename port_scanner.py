import socket
import threading
import queue
import argparse


port_queue = queue.Queue()
print_lock = threading.Lock()


common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            with print_lock:
                if result == 0:
                    service = common_ports.get(port, "Unknown")
                    print(f"[+] Port {port} is open ({service})")
    except Exception as e:
        pass  
def threader(ip):
    while True:
        port = port_queue.get()
        scan_port(ip, port)
        port_queue.task_done()

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded Port Scanner")
    parser.add_argument("host", help="Target host to scan (IP or domain)")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")

    args = parser.parse_args()
    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"[!] Invalid host: {args.host}")
        return

    print(f"Scanning {args.host} ({target_ip}) from port {args.start} to {args.end}")

    # Start threads
    for _ in range(args.threads):
        t = threading.Thread(target=threader, args=(target_ip,))
        t.daemon = True
        t.start()

    for port in range(args.start, args.end + 1):
        port_queue.put(port)

    port_queue.join()
    print("Scan complete.")

if __name__ == "__main__":
    main()
