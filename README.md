# Multi-Thread Port Scanner

A high-performance multi-threaded port scanner written in Python. This tool allows users to quickly scan multiple ports across one or more target hosts, utilizing the power of threading to speed up the scanning process.

## Features

- Scans multiple ports on single or multiple hosts
- Utilizes threading for faster scanning
- Customizable thread count
- Supports scanning port ranges and lists
- Reports open ports in real-time
- Simple and easy-to-use command-line interface

## Requirements

- Python 3.6 or higher

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/multi-thread-port-scanner.git
cd multi-thread-port-scanner
```

(Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py -t <target> -p <ports> [-T <threads>]
```

### Arguments

- `-t`, `--target`: Target IP address or hostname (required, supports comma-separated values for multiple targets)
- `-p`, `--ports`: Ports to scan (e.g. `80`, `20-100`, `22,80,443`)
- `-T`, `--threads`: Number of threads to use (default: 100)

### Example

Scan ports 22, 80, and 443 on 192.168.1.1 using 200 threads:

```bash
python scanner.py -t 192.168.1.1 -p 22,80,443 -T 200
```

Scan ports 1 to 1024 on multiple hosts:

```bash
python scanner.py -t 192.168.1.1,192.168.1.2 -p 1-1024
```

## Output

Open ports will be printed to the console as soon as they are discovered.

Example output:

```
[192.168.1.1] Port 80 is open
[192.168.1.1] Port 443 is open
[192.168.1.2] Port 22 is open
```

## Notes

- Scanning hosts and ports you do not own or have explicit permission to test may be illegal. Use responsibly.
- Higher thread counts can increase speed but may also result in connection errors or be detected by firewalls.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

This tool is intended for educational and authorized security testing purposes only.
