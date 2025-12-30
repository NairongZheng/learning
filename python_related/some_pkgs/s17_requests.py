"""
requests - Python HTTP库

requests是Python中最常用的HTTP客户端库，让HTTP请求变得简单优雅。
官方文档: https://requests.readthedocs.io/
"""

import requests
from requests.exceptions import RequestException, Timeout, HTTPError


def example_basic_get():
    """基本GET请求"""
    print("=" * 50)
    print("1. 基本GET请求")
    print("=" * 50)
    
    # 简单的GET请求
    response = requests.get('https://httpbin.org/get')
    print(f"状态码: {response.status_code}")
    print(f"响应头: {response.headers}")
    print(f"响应内容: {response.text[:200]}...")
    print(f"JSON数据: {response.json()}")
    print()


def example_get_with_params():
    """带参数的GET请求"""
    print("=" * 50)
    print("2. 带参数的GET请求")
    print("=" * 50)
    
    # 方式1: 拼接URL
    response1 = requests.get('https://httpbin.org/get?key1=value1&key2=value2')
    
    # 方式2: 使用params参数（推荐）
    params = {
        'key1': 'value1',
        'key2': 'value2',
        'name': '张三'
    }
    response2 = requests.get('https://httpbin.org/get', params=params)
    print(f"请求URL: {response2.url}")
    print(f"参数: {response2.json()['args']}")
    print()


def example_post_requests():
    """POST请求"""
    print("=" * 50)
    print("3. POST请求")
    print("=" * 50)
    
    # 发送表单数据
    data = {
        'username': 'admin',
        'password': '123456'
    }
    response = requests.post('https://httpbin.org/post', data=data)
    print(f"表单数据: {response.json()['form']}")
    
    # 发送JSON数据
    json_data = {
        'name': '张三',
        'age': 25,
        'email': 'zhangsan@example.com'
    }
    response = requests.post('https://httpbin.org/post', json=json_data)
    print(f"JSON数据: {response.json()['json']}")
    print()


def example_custom_headers():
    """自定义请求头"""
    print("=" * 50)
    print("4. 自定义请求头")
    print("=" * 50)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
        'Authorization': 'Bearer your_token_here',
        'Custom-Header': 'custom_value'
    }
    response = requests.get('https://httpbin.org/headers', headers=headers)
    print(f"请求头: {response.json()['headers']}")
    print()


def example_cookies():
    """Cookie处理"""
    print("=" * 50)
    print("5. Cookie处理")
    print("=" * 50)
    
    # 发送cookies
    cookies = {
        'session_id': 'abc123',
        'user_token': 'xyz789'
    }
    response = requests.get('https://httpbin.org/cookies', cookies=cookies)
    print(f"发送的Cookies: {response.json()['cookies']}")
    
    # 从响应中获取cookies
    response = requests.get('https://httpbin.org/cookies/set?name=value')
    print(f"响应的Cookies: {response.cookies}")
    print(f"Cookies字典: {requests.utils.dict_from_cookiejar(response.cookies)}")
    print()


def example_session():
    """使用Session保持会话"""
    print("=" * 50)
    print("6. 使用Session保持会话")
    print("=" * 50)
    
    # 创建session对象
    session = requests.Session()
    
    # 设置session级别的headers和cookies
    session.headers.update({'User-Agent': 'My App/1.0'})
    
    # 第一次请求设置cookie
    response1 = session.get('https://httpbin.org/cookies/set?session=active')
    
    # 第二次请求会自动携带cookie
    response2 = session.get('https://httpbin.org/cookies')
    print(f"Session中的Cookies: {response2.json()['cookies']}")
    
    # 关闭session
    session.close()
    print()


def example_timeout():
    """超时设置"""
    print("=" * 50)
    print("7. 超时设置")
    print("=" * 50)
    
    try:
        # 连接超时和读取超时都是3秒
        response = requests.get('https://httpbin.org/delay/2', timeout=3)
        print("请求成功")
    except Timeout:
        print("请求超时")
    
    try:
        # 分别设置连接超时和读取超时
        response = requests.get('https://httpbin.org/delay/5', timeout=(3, 5))
        print("请求成功")
    except Timeout:
        print("请求超时")
    print()


def example_error_handling():
    """错误处理"""
    print("=" * 50)
    print("8. 错误处理")
    print("=" * 50)
    
    try:
        # 请求不存在的页面
        response = requests.get('https://httpbin.org/status/404')
        # 如果状态码不是200，抛出HTTPError
        response.raise_for_status()
    except HTTPError as e:
        print(f"HTTP错误: {e}")
    except RequestException as e:
        print(f"请求错误: {e}")
    print()


def example_file_upload():
    """文件上传"""
    print("=" * 50)
    print("9. 文件上传")
    print("=" * 50)
    
    # 创建临时文件
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("这是测试文件内容")
        temp_file = f.name
    
    # 上传文件
    with open(temp_file, 'rb') as f:
        files = {'file': ('test.txt', f, 'text/plain')}
        response = requests.post('https://httpbin.org/post', files=files)
        print(f"上传成功: {response.json()['files']}")
    
    # 清理临时文件
    import os
    os.unlink(temp_file)
    print()


def example_download_file():
    """下载文件"""
    print("=" * 50)
    print("10. 下载文件")
    print("=" * 50)
    
    # 下载小文件
    response = requests.get('https://httpbin.org/image/png')
    with open('/tmp/downloaded_image.png', 'wb') as f:
        f.write(response.content)
    print("小文件下载完成")
    
    # 流式下载大文件
    url = 'https://httpbin.org/stream-bytes/10240'  # 10KB
    response = requests.get(url, stream=True)
    with open('/tmp/large_file.bin', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("大文件流式下载完成")
    print()


def example_http_methods():
    """各种HTTP方法"""
    print("=" * 50)
    print("11. 各种HTTP方法")
    print("=" * 50)
    
    base_url = 'https://httpbin.org'
    
    # GET
    response = requests.get(f'{base_url}/get')
    print(f"GET: {response.status_code}")
    
    # POST
    response = requests.post(f'{base_url}/post', data={'key': 'value'})
    print(f"POST: {response.status_code}")
    
    # PUT
    response = requests.put(f'{base_url}/put', data={'key': 'value'})
    print(f"PUT: {response.status_code}")
    
    # DELETE
    response = requests.delete(f'{base_url}/delete')
    print(f"DELETE: {response.status_code}")
    
    # PATCH
    response = requests.patch(f'{base_url}/patch', data={'key': 'value'})
    print(f"PATCH: {response.status_code}")
    
    # HEAD
    response = requests.head(f'{base_url}/get')
    print(f"HEAD: {response.status_code}")
    
    # OPTIONS
    response = requests.options(f'{base_url}/get')
    print(f"OPTIONS: {response.status_code}")
    print()


def example_response_properties():
    """响应对象属性"""
    print("=" * 50)
    print("12. 响应对象属性")
    print("=" * 50)
    
    response = requests.get('https://httpbin.org/get')
    
    print(f"状态码: {response.status_code}")
    print(f"是否成功: {response.ok}")  # 状态码 < 400
    print(f"原因: {response.reason}")
    print(f"URL: {response.url}")
    print(f"编码: {response.encoding}")
    print(f"响应头: {dict(list(response.headers.items())[:3])}...")
    print(f"文本内容: {response.text[:100]}...")
    print(f"字节内容: {response.content[:100]}...")
    print(f"JSON内容: {list(response.json().keys())}")
    print()


def example_proxies():
    """使用代理"""
    print("=" * 50)
    print("13. 使用代理")
    print("=" * 50)
    
    # 注意：这只是示例，实际使用需要有效的代理服务器
    proxies = {
        'http': 'http://10.10.10.10:8000',
        'https': 'http://10.10.10.10:8000',
    }
    
    # response = requests.get('https://httpbin.org/ip', proxies=proxies)
    print("代理配置示例（实际使用需要有效的代理服务器）")
    print(f"代理配置: {proxies}")
    print()


def example_ssl_verification():
    """SSL证书验证"""
    print("=" * 50)
    print("14. SSL证书验证")
    print("=" * 50)
    
    # 禁用SSL证书验证（不推荐，仅用于测试）
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    response = requests.get('https://httpbin.org/get', verify=False)
    print("禁用SSL验证请求成功（不推荐）")
    
    # 使用自定义证书
    # response = requests.get('https://example.com', verify='/path/to/cert.pem')
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("requests库使用示例")
    print("=" * 50 + "\n")
    
    example_basic_get()
    example_get_with_params()
    example_post_requests()
    example_custom_headers()
    example_cookies()
    example_session()
    example_timeout()
    example_error_handling()
    example_file_upload()
    example_download_file()
    example_http_methods()
    example_response_properties()
    example_proxies()
    example_ssl_verification()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
