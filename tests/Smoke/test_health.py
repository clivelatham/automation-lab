def test_health_endpoint_returns_ok(base_url, http, timeout):
    response = http.get(f"{base_url}/health", timeout=timeout)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}



