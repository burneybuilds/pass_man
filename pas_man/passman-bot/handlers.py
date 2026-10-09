import httpx as http

def send_request(requested_password):
    data = http.get(f"http://127.0.0.1:8000/passwords/{requested_password}").json()
    return data