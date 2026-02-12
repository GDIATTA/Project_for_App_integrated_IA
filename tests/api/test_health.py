import os, time, requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

def wait_up(url, timeout=60):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 500:
                return
        except Exception:
            pass
        time.sleep(2)
    raise RuntimeError(f"API not ready: {url}")

def test_api_is_up():
    wait_up(f"{BASE_URL}/")
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code in (200, 404)  # adapte selon tes routes

# Si tu as /health, c’est encore mieux :
# def test_health():
#     wait_up(f"{BASE_URL}/health")
#     r = requests.get(f"{BASE_URL}/health")
#     assert r.status_code == 200