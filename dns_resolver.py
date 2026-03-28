import socket
 
def forward_lookup(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return "Could not resolve hostname"

def reverse_lookup(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return result[0]
    except socket.herror:
        return "No PTR record found"

def get_all_ips(hostname):
    try:
        info = socket.getaddrinfo(hostname, 80)
        return list(set(i[4][0] for i in info))
    except socket.gaierror:
        return []

def run_report(hostname, ip):
    print(f"\nTarget: {hostname}")
    print(f"Forward lookup: {forward_lookup(hostname)}")
    print(f"All IPs: {get_all_ips(hostname)}")
    print(f"\nReverse lookup for {ip}: {reverse_lookup(ip)}")

run_report("scanme.nmap.org", "45.33.32.156")
