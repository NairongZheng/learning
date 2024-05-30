"""
测试, 注意看两个post的传参
"""
import requests

def test_sum():
    request = {"para_a": 10, "para_b": 36}
    print(f"debug damonzheng, request:{request}")
    response = requests.post(url="http://localhost:8888/sumHandler", json=request)
    if response.status_code == 200:
        result = response.json()
        if result["errcode"] == 200:
            print("sum result from server:", result["data"])
        elif result["errcode"] == 400:
            print("Server error:", result["data"])
    else:
        print("Failed to connect to server")


def test_upper():
    request = "lower string to upper string"
    print(f"debug damonzheng, request:{request}")
    response = requests.post(url="http://localhost:8888/upperHandler", data=request)
    if response.status_code == 200:
        result = response.json()
        if result["errcode"] == 200:
            print("Uppercase string from server:", result["data"])
        elif result["errcode"] == 400:
            print("Server error:", result["data"])
    else:
        print("Failed to connect to server")


def main():
    test_sum()
    test_upper()


if __name__ == "__main__":
    main()
