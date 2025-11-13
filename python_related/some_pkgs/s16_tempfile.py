import os
import tempfile
import shutil

class FileSystemSandbox:
    """一个简单的文件系统沙箱，用于安全执行文件操作"""
    def __init__(self):
        # 创建沙箱根目录
        self.root = tempfile.mkdtemp(prefix="sandbox_")
        print(f"🧩 沙箱已创建: {self.root}")

    def _safe_path(self, path):
        """确保所有操作都在沙箱内"""
        abs_path = os.path.abspath(os.path.join(self.root, path))
        if not abs_path.startswith(self.root):
            raise PermissionError("⚠️ 禁止访问沙箱外部路径！")
        return abs_path

    def create_file(self, path, content=""):
        abs_path = self._safe_path(path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w") as f:
            f.write(content)
        print(f"✅ 创建文件: {abs_path}")

    def read_file(self, path):
        abs_path = self._safe_path(path)
        with open(abs_path, "r") as f:
            data = f.read()
        print(f"📖 读取文件 {abs_path}: {data}")
        return data

    def delete_file(self, path):
        abs_path = self._safe_path(path)
        if os.path.exists(abs_path):
            os.remove(abs_path)
            print(f"🗑️ 删除文件: {abs_path}")

    def list_files(self, subdir=""):
        abs_path = self._safe_path(subdir)
        for root, dirs, files in os.walk(abs_path):
            for name in files:
                print(os.path.relpath(os.path.join(root, name), self.root))

    def reset(self):
        """清空沙箱"""
        shutil.rmtree(self.root)
        print(f"💥 沙箱已销毁: {self.root}")

# ------------------- 使用示例 -------------------

if __name__ == "__main__":
    sandbox = FileSystemSandbox()
    try:
        sandbox.create_file("logs/test.txt", "Hello Sandbox!")
        sandbox.read_file("logs/test.txt")
        sandbox.list_files()
        # sandbox.create_file("../hack.txt", "Oops!")  # 会抛出安全错误
    finally:
        sandbox.reset()
