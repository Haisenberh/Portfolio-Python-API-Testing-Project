from tests.step_defs.test_api_steps import get_random_email, send_get_request, send_post_request, send_delete_request, verify_response_got_data, verify_response_field_exist, verify_status_code
from tests.config import GOREST_API_TOKEN


def test_get_cat_fact_endpoint():
    response = send_get_request("https://catfact.ninja/fact")
    verify_status_code(response=response, expected_code=200)
    verify_response_got_data(response)
    verify_response_field_exist(response=response, field='length')


def test_post_gorest_endpoint_positive():
    call_headers = {
        "Authorization": f"Bearer {GOREST_API_TOKEN}",
    }
    data = {"name": "Allasani Peddana", "email": get_random_email(), "status": "active", "gender": "male"}
    response = send_post_request(url="https://gorest.co.in/public/v2/users", headers=call_headers, json=data)
    verify_status_code(response=response, expected_code=201)
    verify_response_got_data(response)


def test_gorest_delete_endpoint_positive():
    call_headers = {
        "Authorization": f"Bearer {GOREST_API_TOKEN}",
    }
    response = send_get_request(url=f"https://gorest.co.in/public/v2/users")
    if response.json():
        created_user_id = response.json()[0].get('id')
        response = send_delete_request(url=f"https://gorest.co.in/public/v2/users/{created_user_id}", headers=call_headers)
        verify_status_code(response=response, expected_code=204)
    else:
        raise Exception(f"Can't get users list! Details: {response.text}")


def test_post_gorest_endpoint_negative():
    call_headers = {
        "Authorization": f"Bearer {GOREST_API_TOKEN}",
    }
    data = {"name": "", "email": get_random_email(), "status": "active", "gender": "male"}
    response = send_post_request(url="https://gorest.co.in/public/v2/users", headers=call_headers, json=data)
    print(response.text)
    verify_status_code(response=response, expected_code=422)
    if response.json():
        print("Test error response message is correct")
        assert response.json()[0].get('message') == "can't be blank", f"Fail! Expected filed is not the same as actual! Response: {response.json()}"
        assert response.json()[0].get('field') == "name", f"Fail! Expected filed is not the same as actual! Response: {response.json()}"
