import httpx
from tools.fakers import get_random_email, last_name_generator, first_name_generator, password_generator

generated_password = password_generator()

user_data = {
  "email": get_random_email(),
  "password": generated_password,
  "lastName": last_name_generator(),
  "firstName": first_name_generator(),
  "middleName": last_name_generator(),
}

response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)
print("response:", response.json())
print("Status code:", response.status_code)



payload = {
    "email": response.json()["user"]["email"],
    "password": generated_password
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
print("Login response:", login_response.json())
print("Status Code:", login_response.status_code)

token_header = login_response.json()["token"]["accessToken"]
user_id = response.json()["user"]["id"]

user_data = {
    "email": get_random_email(),
    "lastName": last_name_generator(),
    "firstName": first_name_generator(),
    "middleName": last_name_generator(),
}

update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}",
                            headers={"Authorization": f"Bearer {token_header}"},
                            json=user_data)
print("Update response:", update_response.json())
print("Status Code:", update_response.status_code)
