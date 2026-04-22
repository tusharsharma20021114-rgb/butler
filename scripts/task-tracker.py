#!/usr/bin/env python3
"""
Butler Task Tracker — Manage tasks with priorities and deadlines.

Usage:
    python task-tracker.py init                              # Initialize a new task file
    python task-tracker.py add "Task description" --priority high --due 2026-04-25
    python task-tracker.py list                               # List all tasks
    python task-tracker.py list --filter pending              # Filter by status
    python task-tracker.py done <task-id>                     # Mark task complete
    python task-tracker.py remove <task-id>                   # Remove a task
    python task-tracker.py prioritize                         # Re-sort by urgency
    python task-tracker.py summary                            # Quick summary stats
"""

import json
import sys
import os
from datetime import datetime, date
from pathlib import Path

TASK_FILE = "butler-tasks.json"

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_EMOJI = {"high": "🔴", "medium": "🟡", "low": "🟢"}
STATUS_EMOJI = {"pending": "⬜", "done": "✅", "overdue": "🔥"}


def load_tasks():
    """Load tasks from the JSON file."""
    if not Path(TASK_FILE).exists():
        print(f"❌ No task file found. Run 'python task-tracker.py init' first.")
        sys.exit(1)
    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(data):
    """Save tasks to the JSON file."""
    data["updated_at"] = datetime.now().isoformat()
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_id(tasks):
    """Generate a short incremental task ID."""
    if not tasks:
        return "T001"
    max_id = max(int(t["id"][1:]) for t in tasks)
    return f"T{max_id + 1:03d}"


def init_tasks():
    """Initialize a new task file."""
    if Path(TASK_FILE).exists():
        print(f"⚠️  Task file already exists at {TASK_FILE}")
        return
    data = {
        "version": "1.0",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "tasks": []
    }
    save_tasks(data)
    print(f"✅ Initialized task tracker at {TASK_FILE}")


def add_task(description, priority="medium", due=None, category=None):
    """Add a new task."""
    data = load_tasks()
    task = {
        "id": generate_id(data["tasks"]),
        "description": description,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "due": due,
        "category": category
    }
    data["tasks"].append(task)
    save_tasks(data)
    emoji = PRIORITY_EMOJI.get(priority, "⚪")
    print(f"✅ Added task {task['id']}: {emoji} {description}")
    if due:
        print(f"   📅 Due: {due}")


def list_tasks(filter_status=None):
    """List all tasks, grouped by priority."""
    data = load_tasks()
    tasks = data["tasks"]

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("📭 No tasks found.")
        return

    # Check for overdue tasks
    today = date.today().isoformat()
    for t in tasks:
        if t["status"] == "pending" and t.get("due") and t["due"] < today:
            t["_display_status"] = "overdue"
        else:
            t["_display_status"] = t["status"]

    # Group by priority
    for priority in ["high", "medium", "low"]:
        group = [t for t in tasks if t["priority"] == priority]
        if not group:
            continue
        emoji = PRIORITY_EMOJI[priority]
        print(f"\n{emoji} {priority.upper()} PRIORITY")
        print("─" * 50)
        for t in group:
            status_em = STATUS_EMOJI.get(t.get("_display_status", t["status"]), "⬜")
            due_str = f" 📅 {t['due']}" if t.get("due") else ""
            cat_str = f" [{t['category']}]" if t.get("category") else ""
            strike = "~~" if t["status"] == "done" else ""
            print(f"  {status_em} {t['id']}: {strike}{t['description']}{strike}{due_str}{cat_str}")

    # Summary
    total = len(data["tasks"])
    done = sum(1 for t in data["tasks"] if t["status"] == "done")
    pending = total - done
    overdue = sum(1 for t in data["tasks"]
                  if t["status"] == "pending" and t.get("due") and t["due"] < today)
    print(f"\n📊 Total: {total} | ✅ Done: {done} | ⬜ Pending: {pending} | 🔥 Overdue: {overdue}")


def mark_done(task_id):
    """Mark a task as complete."""
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id.upper():
            task["status"] = "done"
            task["completed_at"] = datetime.now().isoformat()
            save_tasks(data)
            print(f"✅ Completed: {task['description']}")
            return
    print(f"❌ Task {task_id} not found.")


def remove_task(task_id):
    """Remove a task."""
    data = load_tasks()
    original_len = len(data["tasks"])
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id.upper()]
    if len(data["tasks"]) < original_len:
        save_tasks(data)
        print(f"🗑️  Removed task {task_id}")
    else:
        print(f"❌ Task {task_id} not found.")


def prioritize_tasks():
    """Re-sort tasks by priority and due date."""
    data = load_tasks()
    data["tasks"].sort(key=lambda t: (
        0 if t["status"] == "pending" else 1,
        PRIORITY_ORDER.get(t["priority"], 99),
        t.get("due") or "9999-12-31"
    ))
    save_tasks(data)
    print("🔄 Tasks re-prioritized.")
    list_tasks()


def summary():
    """Print a quick summary of task stats."""
    data = load_tasks()
    tasks = data["tasks"]
    today = date.today().isoformat()

    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "done")
    pending = total - done
    overdue = sum(1 for t in tasks
                  if t["status"] == "pending" and t.get("due") and t["due"] < today)
    high = sum(1 for t in tasks if t["priority"] == "high" and t["status"] == "pending")

    print("📋 Butler Task Summary")
    print("═" * 30)
    print(f"  Total tasks:     {total}")
    print(f"  ✅ Completed:    {done}")
    print(f"  ⬜ Pending:      {pending}")
    print(f"  🔴 High priority: {high}")
    print(f"  🔥 Overdue:      {overdue}")

    if total > 0:
        pct = (done / total) * 100
        bar_len = 20
        filled = int(bar_len * done / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  Progress: [{bar}] {pct:.0f}%")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init_tasks()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task-tracker.py add \"Task description\" [--priority high|medium|low] [--due YYYY-MM-DD] [--category name]")
            sys.exit(1)
        desc = sys.argv[2]
        priority = "medium"
        due = None
        category = None
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--priority" and i + 1 < len(sys.argv):
                priority = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--due" and i + 1 < len(sys.argv):
                due = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--category" and i + 1 < len(sys.argv):
                category = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        add_task(desc, priority, due, category)
    elif command == "list":
        filter_status = None
        if "--filter" in sys.argv:
            idx = sys.argv.index("--filter")
            if idx + 1 < len(sys.argv):
                filter_status = sys.argv[idx + 1]
        list_tasks(filter_status)
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: python task-tracker.py done <task-id>")
            sys.exit(1)
        mark_done(sys.argv[2])
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: python task-tracker.py remove <task-id>")
            sys.exit(1)
        remove_task(sys.argv[2])
    elif command == "prioritize":
        prioritize_tasks()
    elif command == "summary":
        summary()
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
