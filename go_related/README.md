# go相关

1. simple_go：简单的go示例
2. connection：各种通信相关案例


## 高亮设置
vscode高亮设置：`文件——首选项——设置——golang——setting.json`
```python
"gopls": {
    "ui.semanticTokens": true
}
```

## go项目
1. 在项目路径下使用`go mod init <module_name>`，如在`udp_here`下使用`go mod init udp_here`，会自动生成`go.mod`
2. 运行模块管理，自动安装需要的包：`go mod tidy`，会自动生成`go.sum`
3. 运行代码：`go run <go_file.go>`
4. 学习go看看`go_related/connection/grpc_connect`和`go_related/connection/grpc_connect2`下的代码，不难，特别是`grpc_connect2`的client代码


## go学习

**Go by Example（官方推荐）**

地址：https://gobyexample.com/
内容：每一章都是一个“最小可运行示例”，涵盖 fmt、os、http、json、concurrency 等常用标准库。
强烈推荐初学者看这个，实用且简洁！

**Go Tour（A Tour of Go）（官方交互式课程）**

地址：https://go.dev/tour
内容：提供交互式练习，包含基础语法、方法、接口、并发、错误处理等。
可以在线练习，不需要安装本地环境。
如果你希望“理论 + 操作”，这是最好的入门路径。

**Go 官方代码库 go.dev 示例项目**

地址：https://pkg.go.dev/std
每个标准库页面下都有 usage 示例，比如：
`fmt`：https://pkg.go.dev/fmt
`net/http`：https://pkg.go.dev/net/http
`encoding/json`：https://pkg.go.dev/encoding/json
点进去可以看到“Examples”字段，展示了如何使用这个包的完整代码片段。

**Go 语言工作坊（Go Workshop by the community）**

地址：https://github.com/golang-workshops
内容：包括 Web 项目、CLI 项目、JSON API 服务器等，从零搭建。
这些适合在掌握基础后动手做项目练习。

**Go Patterns（Go语言设计模式）**

地址：https://github.com/tmrts/go-patterns
内容：不是项目，而是 Go 编程常见模式的集合，包括标准库用法。

**Gophercises（练习项目）**

地址：https://gophercises.com/
内容：非官方，但非常高质量，由 Jon Calhoun 创建。
涵盖文件操作、CLI、HTTP API、数据库、并发等领域。

<!-- ### pkg

<details>
<summary></summary>

<br>


</details> -->
