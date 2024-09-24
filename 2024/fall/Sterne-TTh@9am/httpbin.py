import requests
import json

# Base URL for httpbin
base_url = "https://httpbin.org"

# 1. Basic Auth
def basic_auth():
    username = "testuser"
    password = "testpass"
    auth_url = f"{base_url}/basic-auth/{username}/{password}"
    
    response = requests.get(auth_url, auth=(username, password))
    print("Basic Auth Response:")
    print(json.dumps(response.json(), indent=2))
    print(f"Status Code: {response.status_code}\n")

# 2. Download an image
def download_image():
    image_url = f"{base_url}/image/png"
    response = requests.get(image_url)
    print("Image Download Response:")
    print(f"Content Type: {response.headers['Content-Type']}")
    print(f"Content Length: {response.headers['Content-Length']} bytes")
    print(f"Status Code: {response.status_code}")
    
    # Save the image
    with open("downloaded_image.png", "wb") as f:
        f.write(response.content)
    print("Image saved as 'downloaded_image.png'\n")

# 3. Generate a UUID4
def generate_uuid():
    uuid_url = f"{base_url}/uuid"
    response = requests.get(uuid_url)
    print("UUID Generation Response:")
    print(json.dumps(response.json(), indent=2))
    print(f"Status Code: {response.status_code}\n")

# 4. Return a simple JSON response
def get_json():
    json_url = f"{base_url}/json"
    response = requests.get(json_url)
    print("JSON Response:")
    print(json.dumps(response.json(), indent=2))
    print(f"Status Code: {response.status_code}\n")

if __name__ == "__main__":
    basic_auth()
    download_image()
    generate_uuid()
    get_json()