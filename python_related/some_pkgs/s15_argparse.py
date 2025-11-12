"""
python s15_argparse.py add "Learn argparse" -d "Practice Python CLI" -p 1
python s15_argparse.py list
python s15_argparse.py done 1
python s15_argparse.py delete 1
"""

import argparse

def get_parser():
    # 创建主解析器
    parser = argparse.ArgumentParser(
        description="Task Manager CLI — manage your tasks easily from the command line."
    )

    # 创建子命令解析器集合
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # === 子命令1：add ===
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Title of the task")
    add_parser.add_argument("-d", "--desc", type=str, default="", help="Description of the task")
    add_parser.add_argument("-p", "--priority", type=int, choices=[1, 2, 3], default=2, help="Priority (1=high, 2=medium, 3=low)")

    # === 子命令2：list ===
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("-a", "--all", action="store_true", help="Show completed tasks too")

    # === 子命令3：done ===
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID to mark as done")

    # === 子命令4：delete ===
    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")
    
    return parser

def main():
    # 解析命令行参数
    parser = get_parser()
    args = parser.parse_args()
    
    # 如果没有输入子命令，打印帮助信息
    if not args.command:
        parser.print_help()
        return

    # 调度到具体命令函数
    if args.command == "add":
        add_task(args.title, args.desc, args.priority)
    elif args.command == "list":
        list_tasks(args.all)
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "delete":
        delete_task(args.id)

# === 模拟数据库 ===
tasks = []
completed = []

def add_task(title, desc, priority):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "desc": desc, "priority": priority})
    print(f"✅ Added task #{task_id}: {title}")

def list_tasks(show_all):
    print("📋 Task List:")
    for t in tasks:
        print(f"  [{t['id']}] {t['title']} (priority {t['priority']})")
    if show_all:
        for t in completed:
            print(f"  [✓] {t['title']} (done)")

def mark_done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            completed.append(t)
            print(f"🎯 Task #{task_id} marked as done.")
            return
    print(f"⚠️  Task #{task_id} not found.")

def delete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            print(f"🗑️  Task #{task_id} deleted.")
            return
    print(f"⚠️  Task #{task_id} not found.")

if __name__ == "__main__":
    main()
