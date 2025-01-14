# go相关

1. connection：各种通信相关案例


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
