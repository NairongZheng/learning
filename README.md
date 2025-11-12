- [learning](#learning)
  - [目录](#目录)
  - [vscode 调试](#vscode-调试)


# learning

## 目录

学习的时候看的代码。都是参考别人的
1. ai_related：ai相关
   1. models：models相关的学习
   2. GANs：各种经典GAN
   3. ddp：pytorch分布式训练
   4. rl：强化学习
2. python_related：python编程相关
   1. threading：多线程
   2. pyqt：pyqt
   3. connection：各种通信相关案例, 包括socket, http, 还有grpc
   4. decorator：装饰器
   5. magic_fun_attr：魔术方法与魔术属性
   6. some_pkgs：python一些包的使用
3. cpp_related：cpp编程相关
   1. connection：各种通信相关案例
4. go_related：go编程相关
   1. simple_go：简单的go示例
   2. connection：各种通信相关案例
5. frontend_related：前端相关
   1. html：html和css
6. lc：leetcode刷题


## vscode 调试

在 `.vscode` 中 需要有 `launch.json` 文件，如果需要依赖于某 task 之后再调试，还需要 `tasks.json` 文件 （下面会给例子，这边先对字段进行解释）

**tasks.json**

> | 字段             | 含义                         | 示例/说明                                                                                              |
> | ---------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------ |
> | `version`        | VS Code 任务系统版本号       | 固定为 "2.0.0"                                                                                         |
> | `tasks`          | 定义任务列表的数组           | 里面每个对象是一项任务                                                                                 |
> | -                | -                            | -                                                                                                      |
> | `label`          | 任务名（唯一标识）           | "Add a task"，可被 launch.json 引用                                                                    |
> | `type`           | 任务执行类型                 | "shell"（默认，表示在系统的 shell 中执行）、"process"、"npm"、"gulp"、"make"、"python"（依赖插件）等行 |
> | `command`        | 要运行的命令                 | "python", "npm", "go", "make"                                                                          |
> | `args`           | 命令行参数数组（按顺序传入） | 等价于 python task_cli.py add ...                                                                      |
> | `problemMatcher` | 错误匹配规则（可忽略）       | 空数组即可                                                                                             |
> | `dependsOn`      | 当前任务依赖的任务列表       | "Add then list tasks" 依赖前两个任务                                                                   |
> | `dependsOrder`   | 指定依赖任务执行顺序         | "sequence" 表示按顺序执行                                                                              |

**launch.json**

> | 字段             | 含义                     | 示例/说明                                                            |
> | ---------------- | ------------------------ | -------------------------------------------------------------------- |
> | `version`        | VS Code 调试配置文件版本 | 固定为 "0.2.0"                                                       |
> | `configurations` | 调试配置数组             | **每个对象是一种调试方式**                                           |
> | -                | -                        | -                                                                    |
> | `name`           | 调试配置名               | **在 VS Code 调试面板下拉菜单中显示**                                |
> | `type`           | 调试器类型               | "debugpy", "cppdbg", "node", "go", "java", "pwa-chrome", "docker" 等 |
> | `request`        | 调试请求类型             | "launch"（启动程序） / "attach"（附加到已有进程）                    |
> | `program`        | 要运行的 Python 脚本路径 | ${workspaceFolder}/{xxx}.py                                          |
> | `args`           | 传给脚本的命令行参数     | 这里调试 list 子命令                                                 |
> | `cwd`            | 工作目录                 | "${workspaceFolder}"                                                 |
> | `env`            | 环境变量                 | { "DEBUG": "1", "PORT": "8080" }                                     |
> | `envFile`        | 从文件加载环境变量       | "${workspaceFolder}/.env"                                            |
> | `console`        | 输出控制台位置           | "internalConsole" / "integratedTerminal" / "externalTerminal"        |
> | `stopOnEntry`    | 是否在入口暂停           | true / false                                                         |
> | `justMyCode`     | 是否只调试用户代码       | true（跳过库代码）                                                   |
> | `preLaunchTask`  | **调试前自动执行的任务** | 这里引用了 "Add then list tasks"                                     |
> | `module`         | 指定以模块形式运行       | "flask"（等价于 python -m flask）                                    |
> | `python`         | 指定 Python 解释器路径   | "/usr/bin/python3"（仅 Python 调试器支持）                           |
> | `logToFile`      | 是否将调试日志写入文件   | true                                                                 |

**流程**

> 1. 选择要调试的配置名开始调试（如例子中的 `Debug: Add then List Tasks`）
> 2. 检查 preLaunchTask，若有，需要先运行依赖的 tasks，会先去 `tasks.json` 查找这个任务（如例子中的`Add then list tasks`）
> 3. 找到任务后查看该任务的 dependsOn，若有，依据指定执行顺序执行（如例子中的 `Add then list tasks` 依赖 `Add a task` 和 `List tasks`）
> 4. 执行完所有依赖的 tasks 之后，就可以诶开始执行当前的 debug 任务

`tasks.json` 例子：

```shell
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Add a task",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
                "add",
                "Learn argparse",
                "-d",
                "Practice CLI debugging",
                "-p",
                "1"
            ],
            "problemMatcher": []
        },
        {
            "label": "List tasks",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
                "list"
            ],
            "problemMatcher": []
        },
        {
            "label": "Add then list tasks",
            "dependsOn": [
                "Add a task",
                "List tasks"
            ],
            "dependsOrder": "sequence",
            "problemMatcher": []
        }
    ]
}
```

launch.json 例子：

```shell
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Run CLI (no args)",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Run CLI: add task",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
            "args": [
                "add",
                "Learn argparse",
                "-d",
                "Practice CLI tools",
                "-p",
                "1"
            ],
            "console": "integratedTerminal"
        },
        {
            "name": "Run CLI: list tasks",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
            "args": [
                "list"
            ],
            "console": "integratedTerminal"
        },
        {
            "name": "Debug: Add then List Tasks",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/python_related/some_pkgs/s15_argparse.py",
            "args": [
                "list"
            ],
            "console": "integratedTerminal",
            "preLaunchTask": "Add then list tasks"
        }
    ]
}
```