scan = {"192.168.3.10":"80","192.168.3.11":"443","192.168.3.55":"22"}

for item in scan.items():
    print(scan.items())
    
# Code from guide
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")