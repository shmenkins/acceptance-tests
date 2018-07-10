import requests
import configparser
import json

cfg = configparser.ConfigParser()
cfg.read("config.ini")
_api_url = str(cfg["default"]["api_url"])


def test_post_scm_repo():
    response = requests.post(f"{_api_url}/scm-repos", json={"url": "abc"})

    assert response.status_code == 201

    body = response.json()

    assert body["url"] == "abc"
    assert body["id"] > 0
