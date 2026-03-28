import requests
import os

API_KEY = os.environ.get("VT_API_KEY", "")

def check_ip(ip):
    if not API_KEY:
        print("Set your API key: export VT_API_KEY=your_key")
        return

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": API_KEY}

    try:
        res = requests.get(url, headers=headers, timeout=15)

        if res.status_code != 200:
            print(f"Error: {res.status_code}")
            return

        attrs = res.json()["data"]["attributes"]
        stats = attrs["last_analysis_stats"]
        malicious = stats.get("malicious", 0)
        total = sum(stats.values())

        print(f"\nIP: {ip}")
        print(f"Country: {attrs.get('country', 'unknown')}")
        print(f"Owner: {attrs.get('as_owner', 'unknown')}")
        print(f"Malicious: {malicious} / {total}")
        print(f"Reputation score: {attrs.get('reputation', 0)}")

        if malicious >= 5:
            print("Verdict: HIGH RISK")
        elif malicious >= 1:
            print("Verdict: SUSPICIOUS")
        else:
            print("Verdict: Clean")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

check_ip("45.33.32.156")