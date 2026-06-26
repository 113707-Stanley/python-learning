import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Status Code: {response.status_code} ✅")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
else:
    print(f"Request failed with status code: {response.status_code} ❌")