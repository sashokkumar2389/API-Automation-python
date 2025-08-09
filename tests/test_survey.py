
import requests
import pytest
from utils.headers import get_headers
from utils.payloads import get_payload


def test_create_survey_response():
    url = "https://api.surveymonkey.com/v3/surveys"
    headers = get_headers()
    payload = get_payload()
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 0.5
    try:
        data = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")
    assert isinstance(data, dict)


def test_create_survey_invalid():
    url = "https://api.surveymonkey.com/v3/surveys"
    headers = get_headers()
    payload = '{}'
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code != 201
    try:
        data = response.json()
    except ValueError:
        pytest.fail("Error response is not valid JSON")
    assert isinstance(data, dict)
