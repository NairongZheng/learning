"""
    线程安全问题
"""

import threading
import time

lock = threading.Lock()

class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    with lock:                  # 加了这个就可以解决安全问题、打印问题，可以把这个注释了试试
        if account.balance >= amount:
            time.sleep(0.1)     # sleep一下，让线程切换，看看安全问题（每次都会取钱成功，即使钱不够）
            print(threading.current_thread().name, "取钱成功")
            
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)

        else:
            print(threading.current_thread().name, "取钱失败，余额不足")


def main():
    account = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(account, 800))
    tb = threading.Thread(name='tb', target=draw, args=(account, 800))

    ta.start()
    tb.start()


if __name__ == '__main__':
    main()