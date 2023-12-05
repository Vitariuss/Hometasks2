import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def config():
    with open("C:/Users/Vit/Desktop/Python/New12/config.yaml") as file:
        config_data = yaml.safe_load(file)
    return config_data

@pytest.fixture(scope="session")
def auth_token(config):
    url = config["login_url"]
    username = config["username"]
    password = config["password"]
    response = requests.post(url, json={"username": username, "password": password})
    response.raise_for_status()
    return response.json()["token"]

@pytest.fixture
def post_title(request):
    return request.param

def test_create_post_and_check_description(auth_token):
    url = "https://test-stand.gb.ru/api/posts"
    headers = {
        "X-Auth-Token": auth_token
    }
    data = {
        "title": "Новый пост",
        "description": "Описание нового поста",
        "content": "Содержимое нового поста"
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201  

    
    response = requests.get(url, headers=headers)
    assert response.status_code == 200  
    posts = response.json()
    assert any(post["description"] == data["description"] for post in posts)  