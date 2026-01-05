import pytest

@pytest.mark.parametrize(
    "route, expected_status",
    [
        ("/health", 200),
        ("/version", 200),
        ("/does-not-exist", 404),
    ],
)
def test_routes_return_expected_status(base_url, http, timeout, route, expected_status):
    response = http.get(f"{base_url}{route}", timeout=timeout)

    assert response.status_code == expected_status

