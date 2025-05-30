

# server
server提供两个服务，分别用不同的写法实现，两种写法区别有(来自GPT)：
## 区别一
是否用`pydantic`的`BaseModel`定义了请求和返回的格式
1. 如果使用pydantic.BaseModel进行请求和响应的验证，可以确保数据格式正确。
2. 不定义额外的pydantic.BaseModel模型，直接处理JSON数据，代码简洁。
## 区别二
想要获取client的ip跟port，是否需要定义额外参数
限制请求跟响应类型的话就需要显示传个`Request`来获得ip跟port
1. 如果只传递了一个`request`参数，直接在一个参数上操作，更简单，但在处理复杂请求时可能显得不够灵活。
2. 如果使用了两个参数，可能在需要获取更多请求信息时更灵活，例如需要同时处理多个请求对象时。但由于传递了额外的参数，代码显得有些冗余，特别是当仅仅为了获取IP和端口时。
## 区别三
是否真正使用了`async`跟`await`
1. `sumHandler`虽然定义为异步函数，但实际操作（简单的加法计算）并不需要异步处理，显得有些多余。
2. `upperHandler`通过await关键字处理异步请求，使得代码在处理I/O操作时更高效。

## 总结
对于大多数场景来说，`upper_handler`的写法更为简洁和直接，**推荐**使用这种方式来获取请求的IP和端口。
如果在某些特定场景下需要传递多个请求对象，可以考虑使用类似`sum_handler`的写法，**但这不是常见需求**。