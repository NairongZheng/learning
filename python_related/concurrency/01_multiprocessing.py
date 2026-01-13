"""
多进程示例

两个最常见的场景：
- 模拟**批量图像处理**（CPU 密集型）
- 模拟**处理很大的 jsonl 数据**（CPU 密集型解析 / 特征计算）
"""

import json
import math
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
from tqdm import tqdm


# ==================== 场景 1：批量图像处理（模拟） ====================
def fake_image_process(image_id: int, size: int = 900) -> str:
    """
    模拟图像处理：
    - 假设有一张 size x size 的图片
    - 对每个像素做一点“复杂计算”（这里用 sqrt + sin 之类）
    """
    total = 0.0
    for i in range(size):
        for j in range(size):
            total += math.sqrt(i * j + 1)
    return f"image_{image_id} done, total={total:.2f}"


def example_image_processing(num_images: int, image_size: int) -> None:
    print("=" * 50)
    print("示例 1：批量图像处理（模拟，无文件 IO）")
    print("=" * 50)

    image_ids = list(range(1, num_images + 1))

    # 单进程
    start = time.time()
    # 注意：这里 size 越大，单个任务越"重"，多进程越容易体现优势
    single_results = [fake_image_process(img_id, size=image_size) for img_id in image_ids]
    single_time = time.time() - start
    print(f"单进程处理 {len(image_ids)} 张图片耗时: {single_time:.3f} 秒")

    # 多进程（进程池）
    pool_workers = cpu_count()
    pool_workers = max(1, min(pool_workers, len(image_ids)))  # 防止进程数大于任务数

    start = time.time()
    with ProcessPoolExecutor(max_workers=pool_workers) as executor:
        futures = [
            executor.submit(fake_image_process, img_id, image_size)
            for img_id in image_ids
        ]
        multi_results = [future.result() for future in futures]
    multi_time = time.time() - start
    print(f"多进程处理 {len(image_ids)} 张图片耗时: {multi_time:.3f} 秒")
    print(f"加速比: {single_time / multi_time:.2f}x")


# ==================== 场景 2：处理很大的 jsonl 数据（模拟） ====================
def fake_jsonl_record(index: int, values_length: int = 10000) -> str:
    """
    构造一条 jsonl 的"行字符串"（这里只是模拟，实际不用写入文件）
    
    Args:
        index: 记录索引
        values_length: values 数组的长度，越大计算越重
    """
    data = {
        "id": index,
        "text": "hello world " * 20,
        # values 越长，单条记录的计算越"重"，多进程越容易体现优势
        "values": list(range(values_length)),  # 模拟一长串数值
    }
    return json.dumps(data, ensure_ascii=False)


def heavy_parse_and_compute(line: str) -> float:
    """
    模拟对一条 jsonl 记录做“重解析 + 特征计算”：
    - json.loads：模拟解析 json
    - 遍历 values 做一堆数学运算
    """
    obj = json.loads(line)
    s = 0.0
    for v in obj["values"]:
        s += math.sqrt(v + 1) * math.sin(v)
    return s


def example_big_jsonl_processing(num_records: int, values_length: int) -> None:
    print("=" * 50)
    print("示例 2：处理很大的 jsonl 数据（模拟，无文件 IO）")
    print("=" * 50)

    jsonl_lines = [fake_jsonl_record(i, values_length=values_length) for i in range(num_records)]
    tasks = jsonl_lines

    # 单进程处理
    start = time.time()
    single_results = []
    for line in tqdm(jsonl_lines, total=len(jsonl_lines), desc="单进程处理 jsonl 记录"):
        single_results.append(heavy_parse_and_compute(line))
    single_time = time.time() - start
    print(f"单进程处理 {len(jsonl_lines)} 条 jsonl 记录耗时: {single_time:.3f} 秒")

    # 多进程处理（使用 submit + as_completed + tqdm，可以一边计算一边更新进度条）
    pool_workers = cpu_count()
    pool_workers = max(1, min(pool_workers, len(tasks)))  # 防止进程数大于任务数

    start = time.time()
    with ProcessPoolExecutor(max_workers=pool_workers) as executor:
        futures = {
            executor.submit(heavy_parse_and_compute, line): line
            for line in tasks
        }
        multi_results = []

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="处理 jsonl 记录",
        ):
            multi_results.append(future.result())
    multi_time = time.time() - start
    print(f"多进程处理 {len(tasks)} 条 jsonl 记录耗时: {multi_time:.3f} 秒")
    print(f"加速比: {single_time / multi_time:.2f}x")


def main():
    print("\n" + "=" * 50)
    print("Python 多进程编程示例")
    print("=" * 50 + "\n")

    # 计算规模设置
    num_images = 50          # 图像数量
    image_size = 900         # 图像尺寸（size x size）
    num_records = 10000      # jsonl 记录总数
    values_length = 10000    # 每条 jsonl 中 values 的长度

    example_image_processing(num_images=num_images, image_size=image_size)
    example_big_jsonl_processing(num_records=num_records, values_length=values_length)

    print("=" * 50)
    print("示例运行完成")
    print("=" * 50)


if __name__ == "__main__":
    main()
