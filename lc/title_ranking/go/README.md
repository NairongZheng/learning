
- problems：放每一道题的解法跟测试脚本
- utils：放工具函数及测试脚本


**测试**

```bash
go test ${file_dir} -v -run ^{func_name}$
    # ${file_dir}：_test.go所在路径
    # -v：显示testing的日志
    # -run ^{func_name}$：默认是测试整个包中的所有_test.go文件，这边可以指定测试的函数
go test ./utils -v -run ^TestReverse$
```