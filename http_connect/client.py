import requests


def send_request():
    data = "Enter a string"
    response = requests.post("http://localhost:8888/", data=data)
    if response.status_code == 200:
        result = response.json()
        if result["success"]:
            print("Uppercase string from server:", result["data"])
        else:
            print("Server error:", result["error"])
    else:
        print("Failed to connect to server")


if __name__ == "__main__":
    send_request()
