import requests
from behave import given, when, then

# Contexto para almacenar información entre pasos
BASE_URL = "https://dragonball-api.com/api/"

@given("the user set the base url and headers")
def step_set_base_url_and_headers(context):
    context.base_url = BASE_URL
    context.headers = {"Content-Type": "application/json"}

@when("the user send the GET request to {api}")
def step_send_get_request(context, api):
    url = context.base_url + api.strip("'")
    print(f"Sending GET request to: {url}")
    response = requests.get(url, headers=context.headers)
    context.response = response
    print(f"Response JSON: {response.json()}")

@then("the service should return goku character")
def step_validate_goku_character(context):
    assert context.response.status_code == 200, f"Expected status 200 but got {context.response.status_code}"
    data = context.response.json()
    print(f"Validating character name: {data.get('name')}")
    assert data.get("name").lower() == "goku", f"Expected character 'Goku' but got {data.get('name')}"

@then("the service should return vegeta character")
def the_services_should_return_vegeta_character(context):
    assert context.response.status_code == 200, f"Expected status 200 but got {context.response.status_code}"
    data = context.response.json()
    print(f"Validating character name: {data.get('name')}")
    assert data.get("name").lower() == "vegeta", f"Expected character 'Vegeta' but got {data.get('name')}"
