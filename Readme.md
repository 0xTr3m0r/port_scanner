# Port Scanner 
# A simple port scanner written in Python
# Usage
```bash
chmod +x scipt.py
python script.py <ip_address>
```

# features
- Scans a range of ports (1-1024) by default
- use multi-threading to speed up the scanning process
# - Can scan a specific range of ports by passing the `-p` option
```bash
python script.py <ip_address> -p <port_range>
```
# - Can scan a specific port by passing the `-s` option
```bash
python script.py <ip_address> -s <port>
```
