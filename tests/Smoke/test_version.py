def test_version_endpoint_returns_expected_data(base_url, http, timeout):
    response = http.get(f"{base_url}/version", timeout=timeout)

    assert response.status_code == 200
    data = response.json()

    assert data["service"] == "automation-lab"
    assert data["version"] == "1.0.0"








