import requests   # this lirary we are going to use

url = "https://jsonplaceholder.typicode.com/posts/1"

print(requests.get(url))    # prints  <Response [200]> , but it has more info in it e.g. status code, response body, headers, encoding info, etc.

print(requests.get(url).status_code) # prints 200

print(requests.get(url).headers.get('content-type'))  #  prints application/json; charset=utf-8 i.e confirm JSON formate

print(requests.get(url).json())  # parse JSON into a Python dict.

response = requests.get(url)

status_code = response.status_code

if status_code == 200:
    data = response.json()
    print(type(data))     # <class 'dict'>
    for key, value in data.items():
        print(f'{key}: {value}')

else:
    print(f"Request failed with status code {response.status_code}")
