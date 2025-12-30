"""
datetime - 日期和时间处理

datetime模块提供了处理日期和时间的类。
官方文档: https://docs.python.org/3/library/datetime.html
"""

from datetime import datetime, date, time, timedelta, timezone
import time as time_module


def example_basic_usage():
    """基本用法"""
    print("=" * 50)
    print("1. 基本用法 - 创建日期时间对象")
    print("=" * 50)
    
    # 当前日期和时间
    now = datetime.now()
    print(f"当前日期时间: {now}")
    
    # 当前日期
    today = date.today()
    print(f"今天日期: {today}")
    
    # 当前时间
    current_time = datetime.now().time()
    print(f"当前时间: {current_time}")
    
    # 创建特定日期时间
    dt = datetime(2024, 12, 25, 15, 30, 45)
    print(f"特定日期时间: {dt}")
    
    # 创建特定日期
    d = date(2024, 12, 25)
    print(f"特定日期: {d}")
    
    # 创建特定时间
    t = time(15, 30, 45)
    print(f"特定时间: {t}")
    print()


def example_datetime_components():
    """日期时间组成部分"""
    print("=" * 50)
    print("2. 日期时间组成部分")
    print("=" * 50)
    
    dt = datetime(2024, 12, 25, 15, 30, 45, 123456)
    
    print(f"年: {dt.year}")
    print(f"月: {dt.month}")
    print(f"日: {dt.day}")
    print(f"时: {dt.hour}")
    print(f"分: {dt.minute}")
    print(f"秒: {dt.second}")
    print(f"微秒: {dt.microsecond}")
    print(f"星期几: {dt.weekday()} (0=周一, 6=周日)")
    print(f"ISO星期几: {dt.isoweekday()} (1=周一, 7=周日)")
    print()


def example_formatting():
    """格式化输出"""
    print("=" * 50)
    print("3. 格式化输出")
    print("=" * 50)
    
    dt = datetime.now()
    
    # strftime - 日期时间转字符串
    print(f"默认格式: {dt}")
    print(f"YYYY-MM-DD: {dt.strftime('%Y-%m-%d')}")
    print(f"YYYY-MM-DD HH:MM:SS: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"DD/MM/YYYY: {dt.strftime('%d/%m/%Y')}")
    print(f"Month DD, YYYY: {dt.strftime('%B %d, %Y')}")
    print(f"12小时制: {dt.strftime('%I:%M:%S %p')}")
    print(f"星期: {dt.strftime('%A')}")
    print(f"中文格式: {dt.year}年{dt.month}月{dt.day}日 {dt.hour}时{dt.minute}分{dt.second}秒")
    print()


def example_parsing():
    """解析字符串"""
    print("=" * 50)
    print("4. 解析字符串")
    print("=" * 50)
    
    # strptime - 字符串转日期时间
    dt1 = datetime.strptime('2024-12-25', '%Y-%m-%d')
    print(f"解析日期: {dt1}")
    
    dt2 = datetime.strptime('2024-12-25 15:30:45', '%Y-%m-%d %H:%M:%S')
    print(f"解析日期时间: {dt2}")
    
    dt3 = datetime.strptime('25/12/2024', '%d/%m/%Y')
    print(f"解析DD/MM/YYYY: {dt3}")
    
    # ISO格式
    dt4 = datetime.fromisoformat('2024-12-25T15:30:45')
    print(f"ISO格式: {dt4}")
    print()


def example_timedelta():
    """时间差计算"""
    print("=" * 50)
    print("5. 时间差计算 (timedelta)")
    print("=" * 50)
    
    now = datetime.now()
    
    # 创建时间差
    delta = timedelta(days=7, hours=3, minutes=30, seconds=45)
    print(f"时间差: {delta}")
    
    # 日期加减
    future = now + timedelta(days=7)
    print(f"7天后: {future}")
    
    past = now - timedelta(days=30)
    print(f"30天前: {past}")
    
    # 计算两个日期之间的差
    date1 = datetime(2024, 1, 1)
    date2 = datetime(2024, 12, 25)
    diff = date2 - date1
    print(f"\n日期差: {diff}")
    print(f"相差天数: {diff.days}")
    print(f"总秒数: {diff.total_seconds()}")
    
    # 复杂计算
    next_week = now + timedelta(weeks=1)
    print(f"\n下周: {next_week}")
    
    # 时间差的各个组成部分
    delta = timedelta(days=7, hours=3, minutes=30, seconds=45)
    print(f"\n时间差组成:")
    print(f"  天数: {delta.days}")
    print(f"  秒数: {delta.seconds}")
    print(f"  总秒数: {delta.total_seconds()}")
    print()


def example_comparison():
    """日期时间比较"""
    print("=" * 50)
    print("6. 日期时间比较")
    print("=" * 50)
    
    dt1 = datetime(2024, 1, 1)
    dt2 = datetime(2024, 12, 25)
    dt3 = datetime(2024, 1, 1)
    
    print(f"dt1 < dt2: {dt1 < dt2}")
    print(f"dt1 > dt2: {dt1 > dt2}")
    print(f"dt1 == dt3: {dt1 == dt3}")
    print(f"dt1 != dt2: {dt1 != dt2}")
    
    # 判断是否在范围内
    target = datetime(2024, 6, 15)
    start = datetime(2024, 1, 1)
    end = datetime(2024, 12, 31)
    
    if start <= target <= end:
        print(f"\n{target} 在 {start} 和 {end} 之间")
    print()


def example_timezone():
    """时区处理"""
    print("=" * 50)
    print("7. 时区处理")
    print("=" * 50)
    
    # UTC时间
    utc_now = datetime.now(timezone.utc)
    print(f"UTC时间: {utc_now}")
    
    # 带时区的时间
    from datetime import timezone, timedelta
    
    # 东八区（北京时间）
    tz_beijing = timezone(timedelta(hours=8))
    beijing_now = datetime.now(tz_beijing)
    print(f"北京时间: {beijing_now}")
    
    # 转换时区
    utc_time = datetime.now(timezone.utc)
    beijing_time = utc_time.astimezone(tz_beijing)
    print(f"UTC转北京: {beijing_time}")
    
    # 时区信息
    print(f"\n时区名称: {beijing_time.tzname()}")
    print(f"UTC偏移: {beijing_time.utcoffset()}")
    print()


def example_special_dates():
    """特殊日期"""
    print("=" * 50)
    print("8. 特殊日期")
    print("=" * 50)
    
    today = date.today()
    
    # 获取月份第一天
    first_day = today.replace(day=1)
    print(f"本月第一天: {first_day}")
    
    # 获取下个月第一天
    if today.month == 12:
        next_month_first = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month_first = today.replace(month=today.month + 1, day=1)
    print(f"下月第一天: {next_month_first}")
    
    # 获取月份最后一天
    last_day = next_month_first - timedelta(days=1)
    print(f"本月最后一天: {last_day}")
    
    # 获取本周的开始和结束
    weekday = today.weekday()
    week_start = today - timedelta(days=weekday)
    week_end = week_start + timedelta(days=6)
    print(f"本周开始: {week_start}")
    print(f"本周结束: {week_end}")
    
    # 年初和年末
    year_start = date(today.year, 1, 1)
    year_end = date(today.year, 12, 31)
    print(f"今年第一天: {year_start}")
    print(f"今年最后一天: {year_end}")
    print()


def example_timestamp():
    """时间戳"""
    print("=" * 50)
    print("9. 时间戳")
    print("=" * 50)
    
    # 当前时间戳
    now = datetime.now()
    timestamp = now.timestamp()
    print(f"当前时间: {now}")
    print(f"时间戳: {timestamp}")
    
    # 时间戳转datetime
    dt = datetime.fromtimestamp(timestamp)
    print(f"时间戳转datetime: {dt}")
    
    # UTC时间戳
    utc_dt = datetime.utcfromtimestamp(timestamp)
    print(f"UTC时间: {utc_dt}")
    
    # time模块的时间戳
    time_timestamp = time_module.time()
    print(f"time模块时间戳: {time_timestamp}")
    print()


def example_iso_format():
    """ISO格式"""
    print("=" * 50)
    print("10. ISO格式")
    print("=" * 50)
    
    dt = datetime.now()
    
    # 转为ISO格式字符串
    iso_str = dt.isoformat()
    print(f"ISO格式: {iso_str}")
    
    # 日期的ISO格式
    iso_date = dt.date().isoformat()
    print(f"ISO日期: {iso_date}")
    
    # 时间的ISO格式
    iso_time = dt.time().isoformat()
    print(f"ISO时间: {iso_time}")
    
    # ISO周数
    iso_calendar = dt.isocalendar()
    print(f"ISO日历: 年{iso_calendar.year}, 周{iso_calendar.week}, 星期{iso_calendar.weekday}")
    print()


def example_practical_examples():
    """实用示例"""
    print("=" * 50)
    print("11. 实用示例")
    print("=" * 50)
    
    # 1. 计算年龄
    birthday = date(1990, 5, 15)
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    print(f"生日: {birthday}, 年龄: {age}岁")
    
    # 2. 判断是否是闰年
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    year = 2024
    print(f"{year}年是闰年: {is_leap_year(year)}")
    
    # 3. 计算工作日
    def add_business_days(start_date, days):
        current = start_date
        while days > 0:
            current += timedelta(days=1)
            if current.weekday() < 5:  # 周一到周五
                days -= 1
        return current
    
    start = date.today()
    result = add_business_days(start, 5)
    print(f"从{start}开始的5个工作日后: {result}")
    
    # 4. 格式化时间间隔
    def format_timedelta(td):
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days}天 {hours}小时 {minutes}分钟 {seconds}秒"
    
    delta = timedelta(days=2, hours=5, minutes=30, seconds=45)
    print(f"时间间隔: {format_timedelta(delta)}")
    
    # 5. 计算代码执行时间
    start_time = datetime.now()
    time_module.sleep(0.1)  # 模拟耗时操作
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"执行时间: {execution_time.total_seconds()}秒")
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("datetime库使用示例")
    print("=" * 50 + "\n")
    
    example_basic_usage()
    example_datetime_components()
    example_formatting()
    example_parsing()
    example_timedelta()
    example_comparison()
    example_timezone()
    example_special_dates()
    example_timestamp()
    example_iso_format()
    example_practical_examples()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)
