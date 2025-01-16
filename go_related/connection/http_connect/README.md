# http_connect

服务端：
1. `func functionName(w http.ResponseWriter, r *http.Request){}`
   1. `w http.ResponseWriter`：用于将响应数据写回客户端。
   2. `r *http.Request`：表示客户端的请求，包含了请求的所有信息（如请求方法、URL、头部、请求体等）。
2. `err := json.NewDecoder(r.Body).Decode(&request)`
   1. `r.Body`：表示请求体的内容，通常是客户端发送的 JSON 数据。
   2. `.Decode(&request)`：将解析后的数据填充到 request 变量中。
   3. 如果请求体不是合法的 JSON 格式，或字段缺失，会返回一个错误。
3. `w.Header().Set("Content-Type", "application/json")`：设置响应头，告知客户端响应内容是 JSON 格式。
4. `json.NewEncoder(w).Encode(response)`：将 response 对象编码为 JSON 格式，并写入到响应中。

客户端：
1. `resp, err := http.Post(serverHandler, "application/json", bytes.NewBuffer(requestBody))`：发送一个 POST 请求。
   1. `serverHandler`：目标 URL。
   2. `"application/json"`：Content-Type 头，表明请求体是 JSON 数据。
   3. `bytes.NewBuffer(requestBody)`：将 JSON 数据封装为一个 io.Reader 对象，供 POST 方法读取。