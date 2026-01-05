def test_404_response_contract(base_url, http, timeout):
    response = http.get(f"{base_url}/does-not-exist", timeout=timeout)

    assert response.status_code == 404

    # header contract (json)
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()

    # structure contract
    assert isinstance(data, dict)
    assert set(data.keys()) == {"error", "message", "path"}

    # type + value contract
    assert data["error"] == "not_found"
    assert isinstance(data["message"], str)
    assert data["path"] == "/does-not-exist"

