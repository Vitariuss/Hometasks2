import pytest
import requests
from ddt import ddt, data, unpack

@ddt
class TestPosts:
    @pytest.mark.parametrize("post_title", ["Test Post 1", "Test Post 2", "Test Post 3"])
    def test_check_post_exists(self, post_title, auth_token):
        url = "https://test-stand.gb.ru/api/posts"
        headers = {"X-Auth-Token": auth_token}
        params = {"owner": "notMe"}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        posts = response.json()
        assert any(post["title"] == post_title for post in posts)