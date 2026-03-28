# Web Security Toolkit

A collection of Python scripts I built while learning 
web application security and network reconnaissance. 
Each script covers a different concept — DNS resolution, 
HTTP header analysis, session handling, threat intelligence 
lookups, and web fuzzing.

---

## Tools

| Script | What it does |
|--------|-------------|
| `dns_resolver.py` | Forward and reverse DNS lookups |
| `web_requests.py` | HTTP header analysis and security header audit |
| `repeater.py` | HTTP session and POST request demonstration |
| `scan_virus.py` | VirusTotal IP reputation lookup via API |
| `web_bruteforce.py` | Directory fuzzing and SQLi parameter probing |

---

## Setup
```bash
pip install requests
```

For `scan_virus.py` set your VirusTotal API key:
```bash
export VT_API_KEY="your_key_here"
```

Get a free key at [virustotal.com](https://virustotal.com)

---

## Usage
```bash
python dns_resolver.py
python web_requests.py
python repeater.py
python scan_virus.py
python web_bruteforce.py
```

---

## Lab Environment

All scripts were tested in an isolated lab environment. 
`web_bruteforce.py` is configured to run against 
`echo.free.beeceptor.com` — a free echo API that safely 
returns whatever you send it, so nothing touches a real target.

---

## Disclaimer

These tools are for educational purposes only. Only run 
them against systems you own or have explicit permission 
to test. The directory fuzzer and SQLi prober are pointed 
at a safe echo endpoint by default — change the target 
only if you have authorisation.

---

## What I Learned

- How DNS resolution works at the socket level and why 
  multiple IPs suggest a CDN or load balancer
- Which HTTP headers reveal technology stack information 
  and which ones are missing from poorly configured servers
- How session objects persist cookies across requests — 
  the same mechanism an attacker abuses in session hijacking
- How to consume a threat intelligence API and triage 
  an IP address the way a SOC analyst would
- What HTTP response codes mean during directory fuzzing 
  and why a 403 is more interesting than a 404
