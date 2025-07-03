import requests
import pytest
from utils.headers import get_headers
from utils.payloads import get_payload

def get_api_url():
    return "https://api.surveymonkey.com/v3/surveys"

def test_create_survey_response():
    url = get_api_url()
    headers = get_headers()
    payload = get_payload()  # uses random title if not passed

    response = requests.post(url, headers=headers, data=payload)

    # PRIORITY 1: Validate 200 response code
    assert response.status_code == 201, f"Expected 201 OK, got {response.status_code}"

    # PRIORITY 2: Validate response time under 500ms
    assert response.elapsed.total_seconds() < 0.5, f"Response time exceeded 500ms: {response.elapsed.total_seconds()}s"

    # PRIORITY 3: Validate response structure (JSON format)
    try:
        data = response.json()
    except ValueError:
        pytest.fail("Response is not in valid JSON format")

    assert isinstance(data, dict), "Response JSON is not a dictionary"