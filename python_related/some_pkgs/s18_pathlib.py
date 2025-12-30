"""
pathlib - 现代的路径操作库

pathlib提供了面向对象的文件系统路径操作，比传统的os.path更加直观和强大。
官方文档: https://docs.python.org/3/library/pathlib.html
"""

from pathlib import Path
import tempfile
import shutil


def example_basic_usage():
    """基本用法"""
    print("=" * 50)
    print("1. 基本用法")
    print("=" * 50)
    
    # 创建Path对象
    p = Path('/home/user/documents/file.txt')
    print(f"完整路径: {p}")
    print(f"路径字符串: {str(p)}")
    
    # 当前工作目录
    cwd = Path.cwd()
    print(f"当前目录: {cwd}")
    
    # 用户主目录
    home = Path.home()
    print(f"主目录: {home}")
    print()


def example_path_components():
    """路径组成部分"""
    print("=" * 50)
    print("2. 路径组成部分")
    print("=" * 50)
    
    p = Path('/home/user/documents/file.txt')
    
    print(f"完整路径: {p}")
    print(f"父目录: {p.parent}")
    print(f"祖父目录: {p.parent.parent}")
    print(f"所有父目录: {list(p.parents)}")
    print(f"文件名: {p.name}")
    print(f"文件名（不含扩展名）: {p.stem}")
    print(f"扩展名: {p.suffix}")
    print(f"所有扩展名: {p.suffixes}")  # 对于 .tar.gz 等
    print(f"盘符: {p.anchor}")
    print(f"路径部分: {p.parts}")
    print()


def example_path_operations():
    """路径操作"""
    print("=" * 50)
    print("3. 路径操作")
    print("=" * 50)
    
    # 路径拼接 - 使用 / 操作符
    base = Path('/home/user')
    documents = base / 'documents'
    file_path = documents / 'file.txt'
    print(f"拼接路径: {file_path}")
    
    # joinpath方法
    path = Path('/home').joinpath('user', 'documents', 'file.txt')
    print(f"joinpath: {path}")
    
    # 改变文件名
    p = Path('/home/user/file.txt')
    new_p = p.with_name('newfile.txt')
    print(f"改变文件名: {new_p}")
    
    # 改变扩展名
    new_p = p.with_suffix('.md')
    print(f"改变扩展名: {new_p}")
    
    # 改变后缀（保留原有后缀）
    p = Path('/home/user/file.txt')
    new_p = p.with_stem('newfile')
    print(f"改变stem: {new_p}")
    print()


def example_file_operations():
    """文件操作"""
    print("=" * 50)
    print("4. 文件操作")
    print("=" * 50)
    
    # 创建临时目录进行测试
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # 创建文件
        file_path = tmpdir_path / 'test.txt'
        file_path.write_text('Hello, World!\n你好，世界！', encoding='utf-8')
        print(f"文件已创建: {file_path}")
        
        # 读取文件
        content = file_path.read_text(encoding='utf-8')
        print(f"文件内容: {content}")
        
        # 写入字节
        binary_file = tmpdir_path / 'binary.dat'
        binary_file.write_bytes(b'\x00\x01\x02\x03')
        print(f"二进制文件已创建: {binary_file}")
        
        # 读取字节
        binary_content = binary_file.read_bytes()
        print(f"二进制内容: {binary_content}")
        
        # 追加内容
        file_path.write_text(content + 'New line\n', encoding='utf-8')
        print(f"内容已追加")
        
        # 使用open方法
        with file_path.open('r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"文件行数: {len(lines)}")
    print()


def example_directory_operations():
    """目录操作"""
    print("=" * 50)
    print("5. 目录操作")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # 创建目录
        new_dir = tmpdir_path / 'subdir' / 'nested'
        new_dir.mkdir(parents=True, exist_ok=True)
        print(f"目录已创建: {new_dir}")
        
        # 创建文件
        (new_dir / 'file1.txt').write_text('File 1')
        (new_dir / 'file2.py').write_text('# File 2')
        (tmpdir_path / 'root.txt').write_text('Root file')
        
        # 列出目录内容
        print(f"\n列出 {tmpdir_path} 的内容:")
        for item in tmpdir_path.iterdir():
            print(f"  - {item.name} ({'文件' if item.is_file() else '目录'})")
        
        # 递归列出所有文件
        print(f"\n递归列出所有文件:")
        for item in tmpdir_path.rglob('*'):
            if item.is_file():
                print(f"  - {item.relative_to(tmpdir_path)}")
    print()


def example_glob_patterns():
    """通配符匹配"""
    print("=" * 50)
    print("6. 通配符匹配")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # 创建测试文件
        (tmpdir_path / 'file1.txt').touch()
        (tmpdir_path / 'file2.txt').touch()
        (tmpdir_path / 'file3.py').touch()
        (tmpdir_path / 'subdir').mkdir()
        (tmpdir_path / 'subdir' / 'nested.txt').touch()
        
        # glob - 当前目录匹配
        print("所有 .txt 文件:")
        for f in tmpdir_path.glob('*.txt'):
            print(f"  - {f.name}")
        
        # rglob - 递归匹配
        print("\n递归查找所有 .txt 文件:")
        for f in tmpdir_path.rglob('*.txt'):
            print(f"  - {f.relative_to(tmpdir_path)}")
        
        # 匹配模式
        print("\n匹配 file?.txt 模式:")
        for f in tmpdir_path.glob('file?.txt'):
            print(f"  - {f.name}")
    print()


def example_path_checking():
    """路径检查"""
    print("=" * 50)
    print("7. 路径检查")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # 创建测试文件和目录
        file_path = tmpdir_path / 'test.txt'
        file_path.write_text('test')
        dir_path = tmpdir_path / 'subdir'
        dir_path.mkdir()
        symlink_path = tmpdir_path / 'link.txt'
        
        # 各种检查
        print(f"文件存在: {file_path.exists()}")
        print(f"是文件: {file_path.is_file()}")
        print(f"是目录: {file_path.is_dir()}")
        print(f"目录是目录: {dir_path.is_dir()}")
        
        # 不存在的路径
        nonexistent = tmpdir_path / 'nonexistent.txt'
        print(f"不存在的路径: {nonexistent.exists()}")
        
        # 绝对路径和相对路径
        print(f"是绝对路径: {file_path.is_absolute()}")
        relative = Path('relative/path')
        print(f"是绝对路径（相对）: {relative.is_absolute()}")
    print()


def example_file_info():
    """文件信息"""
    print("=" * 50)
    print("8. 文件信息")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        file_path = tmpdir_path / 'test.txt'
        file_path.write_text('Hello, World!' * 100)
        
        # 获取文件信息
        stat = file_path.stat()
        print(f"文件大小: {stat.st_size} 字节")
        print(f"创建时间: {stat.st_ctime}")
        print(f"修改时间: {stat.st_mtime}")
        print(f"访问时间: {stat.st_atime}")
        
        # 文件权限
        print(f"文件模式: {oct(stat.st_mode)}")
    print()


def example_path_resolution():
    """路径解析"""
    print("=" * 50)
    print("9. 路径解析")
    print("=" * 50)
    
    # 相对路径转绝对路径
    relative = Path('.')
    absolute = relative.resolve()
    print(f"相对路径: {relative}")
    print(f"绝对路径: {absolute}")
    
    # 展开用户目录
    user_path = Path('~/documents')
    expanded = user_path.expanduser()
    print(f"用户路径: {user_path}")
    print(f"展开后: {expanded}")
    
    # 相对路径计算
    p1 = Path('/home/user/documents')
    p2 = Path('/home/user/pictures')
    try:
        relative = p1.relative_to(Path('/home/user'))
        print(f"{p1} 相对于 /home/user: {relative}")
    except ValueError:
        print("路径不相关")
    print()


def example_advanced_operations():
    """高级操作"""
    print("=" * 50)
    print("10. 高级操作")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # 重命名
        old_file = tmpdir_path / 'old_name.txt'
        old_file.write_text('content')
        new_file = tmpdir_path / 'new_name.txt'
        old_file.rename(new_file)
        print(f"文件已重命名: {old_file.name} -> {new_file.name}")
        
        # 替换（如果目标存在则覆盖）
        file1 = tmpdir_path / 'file1.txt'
        file2 = tmpdir_path / 'file2.txt'
        file1.write_text('File 1')
        file2.write_text('File 2')
        file1.replace(file2)
        print(f"文件已替换")
        
        # 删除文件
        test_file = tmpdir_path / 'to_delete.txt'
        test_file.write_text('test')
        test_file.unlink()
        print(f"文件已删除")
        
        # 删除空目录
        empty_dir = tmpdir_path / 'empty'
        empty_dir.mkdir()
        empty_dir.rmdir()
        print(f"空目录已删除")
        
        # touch - 创建空文件或更新时间戳
        touch_file = tmpdir_path / 'touched.txt'
        touch_file.touch()
        print(f"文件已touch: {touch_file.name}")
    print()


def example_comparison():
    """与os.path的对比"""
    print("=" * 50)
    print("11. pathlib vs os.path 对比")
    print("=" * 50)
    
    import os
    
    # os.path方式
    old_path = os.path.join('/home', 'user', 'file.txt')
    old_dir = os.path.dirname(old_path)
    old_name = os.path.basename(old_path)
    
    print("os.path方式:")
    print(f"  拼接路径: {old_path}")
    print(f"  目录名: {old_dir}")
    print(f"  文件名: {old_name}")
    
    # pathlib方式
    new_path = Path('/home') / 'user' / 'file.txt'
    new_dir = new_path.parent
    new_name = new_path.name
    
    print("\npathlib方式:")
    print(f"  拼接路径: {new_path}")
    print(f"  目录名: {new_dir}")
    print(f"  文件名: {new_name}")
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("pathlib库使用示例")
    print("=" * 50 + "\n")
    
    example_basic_usage()
    example_path_components()
    example_path_operations()
    example_file_operations()
    example_directory_operations()
    example_glob_patterns()
    example_path_checking()
    example_file_info()
    example_path_resolution()
    example_advanced_operations()
    example_comparison()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
