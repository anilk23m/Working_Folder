import requests
import responses

def mock_user_api():
    responses.add(
        method=responses.GET,
        url="https://api.example.com/users/1",
        json={"id": 1, "name": "Alice"},
        status=200
    )
    responses.add(
        method=responses.POST,
        url="https://api.example.com/resource",
        json={"message": "POST success"},
        status=201
    )

@responses.activate
def test_user_get():
    mock_user_api()  # Call the mock function
    resp = requests.get("https://api.example.com/users/1")
    assert resp.status_code == 200
    print("response status matched")
    assert resp.json()["name"] == "Alice"
    print("json data matched")

@responses.activate
def test_user_post():
    mock_user_api()
    resp = requests.post("https://api.example.com/resource", json={})
    assert resp.status_code == 201
    assert resp.json()["message"] == "POST success"
