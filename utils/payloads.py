import json
import uuid

def get_payload(title=None):
    if title is None:
        title = f"Test survey {uuid.uuid4()}"
    return json.dumps({
        "title": title
    })