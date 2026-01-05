def test_404_response_contract(base_url, http, timeout):
    response = http.get(f"{base_url}/does-not-exist", timeout=timeout)

    assert response.status_code == 404

    data = response.json()

    # contract: must be a JSON object with known keys + value types
    assert isinstance(data, dict)
    assert data["error"] == "not_found"
    assert isinstance(data["message"], str)

