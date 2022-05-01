import random
import string
import requests
from requests.models import Response


def get_random_email():
    return ''.join(random.choice(string.ascii_letters) for _ in range(7)) + "@gmail.com"


def send_get_request(url):
    print(f"Sending get request to url: {url}")
    try:
        result: Response = requests.get(url=url)
        if result:
            return result
    except Exception as e:
        print(f"Got error: {e} while sending get request to {url}")


def send_delete_request(url, headers):
    print(f"Sending delete request to url: {url}")
    try:
        result: Response = requests.delete(url=url, headers=headers)
        if result:
            return result
    except Exception as e:
        print(f"Got error: {e} while sending delete request to {url} with headers: {headers}")


def send_post_request(url, headers, json):
    print(f"Sending post request to url: {url}")
    try:
        result: Response = requests.post(url=url, headers=headers, json=json)
        return result
    except Exception as e:
        print(f"Got error: {e} while sending post request to {url} with headers: {headers} and json: {json}")


def verify_status_code(response, expected_code):
    if response is not None and expected_code is not None:
        print("Test endpoint got valid status code")
        assert response.status_code == expected_code, f"Assert Fail! Expected result {expected_code} is not the same as actual {response.status_code}, details {response.text}"
    else:
        raise Exception(f'Response or expected code is missing! Response: {response}, expected code: {expected_code}')


def verify_response_got_data(response):
    if response:
        print("Verify endpoint got data")
        assert len(response.json()) > 0, f"Fail! Response is empty! Response: {response.json()}"
    else:
        raise Exception('Response is missing!')


def verify_response_field_exist(response, field):
    if response and field:
        print("Verify endpoint got data")
        assert response.json().get(field) is not None, f"Fail! Expected field {field} is not in response: {response.json()}"
    else:
        raise Exception(f'Response or field is missing! Response: {response}, field: {field}')