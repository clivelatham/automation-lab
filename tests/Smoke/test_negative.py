def test_unknown_endpoint_returns_404(base_url, http, timeout):
    response = http.get(f"{base_url}/does-not-exist", timeout=timeout)

    assert response.status_code == 404

