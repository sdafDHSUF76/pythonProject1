import requests

domen = 'http://127.0.0.1:8003'
path = '/api/users'
url = ''.join((domen, path))


def test_job_name_from_request_returns_in_response():
    job = "master"
    name = "morpheus"

    response = requests.post(url, json={"name": name, "job": job})
    body = response.json()
    assert response.status_code == 201
    assert body["name"] == name
    assert body["job"] == job


def test_get_users_returns_unique_users():
    response = requests.get(
        url=url,
        params={"page": 2, "per_page": 4},
        verify=False
    )
    ids = [element["id"] for element in response.json()["data"]]

    assert len(ids) == len(set(ids))
