import httpx

payload = {
    "email": "test12@test.tut",
    "password": "qwerty123!"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()


print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

token_header = login_response.json()["token"]["accessToken"]

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {token_header}"})

print(me_response.json())
print("Status Code:", me_response.status_code)
