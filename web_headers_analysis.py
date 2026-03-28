import requests
 
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "Referrer-Policy",
]

INFO_HEADERS = [
    "Server",
    "X-Powered-By",
    "X-AspNet-Version",
    "X-Generator",
]

def get_headers(url):
    try:
        res = requests.get(url, timeout=10)
        return dict(res.headers), res.status_code
    except requests.RequestException as e:
        print(f"Error: {e}")
        return {}, None

def check_security_headers(headers):
    print("\n-- Security Headers --")
    for header in SECURITY_HEADERS:
        if header in headers:
            print(f"  [present]  {header}: {headers[header][:80]}")
        else:
            print(f"  [missing]  {header}")

def check_info_disclosure(headers):
    print("\n-- Technology Disclosure --")
    found = False
    for header in INFO_HEADERS:
        if header in headers:
            print(f"  [found] {header}: {headers[header]}")
            found = True
    if not found:
        print("  No technology headers disclosed")

def run(url):
    print(f"\nAnalysing: {url}")
    headers, status = get_headers(url)
    if not headers:
        return
    print(f"Status: {status}")
    check_security_headers(headers)
    check_info_disclosure(headers)

run("https://echo.free.beeceptor.com")
