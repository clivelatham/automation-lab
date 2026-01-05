def test_version_response_contract(base_url, http, timeout):
    response = http.get(f"{base_url}/version", timeout=timeout)

    assert response.status_code == 200

    data = response.json()

    # structure checks
    assert isinstance(data, dict)
    assert "service" in data
    assert "version" in data

    # type checks
    assert isinstance(data["service"], str)
    assert isinstance(data["version"], str)


