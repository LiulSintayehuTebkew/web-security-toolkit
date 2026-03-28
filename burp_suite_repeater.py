import requests
 
def send_request(newValue):
    session = requests.Session()

    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Content-Type": newValue
    })

    data = {
        "username": "testuser",
        "password": "TestPassword123"
    }

    try:
        res = session.post("https://echo.free.beeceptor.com", data=data, timeout=10)

        print(f"Status: {res.status_code}")
        print(f"\nResponse Headers:")
        for k, v in res.headers.items():
            print(f"  {k}: {v}")

        cookies = dict(session.cookies)
        if cookies:
            print(f"\nCookies set: {cookies}")
        else:
            print("\nNo cookies set by server")

        print(f"\nResponse body:\n{res.text[:500]}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

contentTpye = input('Enter Content Type: ')

send_request(contentTpye)
