# try, except explanation https://chatgpt.com/share/694d4c38-b654-8002-8418-f772928c9de7
# https://chatgpt.com/share/694d4baf-6e34-8002-80c2-a027be5d2a36

import requests  # import request library

user_id = input("Enter Your ID-number: ")  # getting user_id

try:
    user_id = int(user_id)
    print(f"Valid ID: {user_id}")
except ValueError:
    print("Invalid ID (not a number)")

url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"  # insert the user_id in url

response = requests.get(url)

print(response)  # shows status like <Response [200]>

# print(type(response.json())) # shows data tpe

if response.status_code == 200:
    data = response.json()
    print(type(data))

    for key, value in data.items():
        print(f"{key}: {value}")
else:
    print(f"<Response [404]>: Invalid user_id")