#!/usr/bin/env python3
"""
Butler Daily Planner — Generate structured daily plans with time blocks.

Usage:
    python daily-planner.py "Task 1" "Task 2" "Task 3"
    python daily-planner.py --file tasks.txt
    python daily-planner.py --from-tracker          # Read from butler-tasks.json
    python daily-planner.py "Task 1" --start 09:00 --end 18:00 --breaks 2

Options:
    --start HH:MM     Start time (default: 09:00)
    --end HH:MM       End time (default: 18:00)
    --breaks N        Number of breaks to insert (default: 2)
    --from-tracker    Load pending tasks from butler-tasks.json
    --file PATH       Load tasks from a text file (one per line)
"""

import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_EMOJI = {"high": "🔴", "medium": "🟡", "low": "🟢"}


def parse_time(time_str):
    """Parse HH:MM string to datetime object (using today's date)."""
    today = datetime.now().date()
    hour, minute = map(int, time_str.split(":"))
    return datetime(today.year, today.month, today.day, hour, minute)


def load_tasks_from_tracker():
    """Load pending tasks from butler-tasks.json."""
    tracker_file = Path("butler-tasks.json")
    if not tracker_file.exists():
        print("❌ No butler-tasks.json found. Add tasks first.")
        sys.exit(1)
    with open(tracker_file) as f:
        data = json.load(f)
    pending = [t for t in data["tasks"] if t["status"] == "pending"]
    pending.sort(key=lambda t: PRIORITY_ORDER.get(t.get("priority", "medium"), 1))
    return [(t["description"], t.get("priority", "medium")) for t in pending]


def load_tasks_from_file(filepath):
    """Load tasks from a text file (one per line)."""
    with open(filepath) as f:
        lines = [line.strip() for line in f if line.strip()]
    return [(line, "medium") for line in lines]


def categorize_eisenhower(tasks):
    """Categorize tasks using the Eisenhower Matrix."""
    quadrants = {
        "🔥 DO FIRST (Urgent + Important)": [],
        "📅 SCHEDULE (Important, Not Urgent)": [],
        "👤 DELEGATE (Urgent, Not Important)": [],
        "🗑️ ELIMINATE (Neither)": [],
    }
    for desc, priority in tasks:
        if priority == "high":
            quadrants["🔥 DO FIRST (Urgent + Important)"].append(desc)
        elif priority == "medium":
            quadrants["📅 SCHEDULE (Important, Not Urgent)"].append(desc)
        elif priority == "low":
            quadrants["👤 DELEGATE (Urgent, Not Important)"].append(desc)
        else:
            quadrants["🗑️ ELIMINATE (Neither)"].append(desc)
    return quadrants


def estimate_duration(task_desc):
    """Estimate task duration in minutes based on keywords."""
    desc_lower = task_desc.lower()
    if any(w in desc_lower for w in ["quick", "small", "minor", "check", "review"]):
        return 30
    if any(w in desc_lower for w in ["meeting", "call", "standup", "sync"]):
        return 45
    if any(w in desc_lower for w in ["write", "draft", "create", "build", "develop"]):
        return 90
    if any(w in desc_lower for w in ["research", "analyze", "deep", "complex"]):
        return 120
    return 60  # default


def generate_plan(tasks, start_time="09:00", end_time="18:00", num_breaks=2):
    """Generate a structured daily plan."""
    start = parse_time(start_time)
    end = parse_time(end_time)
    total_minutes = int((end - start).total_seconds() / 60)

    # Estimate durations
    task_blocks = []
    for desc, priority in tasks:
        duration = estimate_duration(desc)
        task_blocks.append({
            "description": desc,
            "priority": priority,
            "duration": duration
        })

    # Calculate break positions
    total_tasks = len(task_blocks)
    break_interval = max(1, total_tasks // (num_breaks + 1))

    # Build the schedule
    current_time = start
    today_str = datetime.now().strftime("%A, %B %d, %Y")

    print(f"# 📋 Daily Plan — {today_str}")
    print(f"**Working hours:** {start_time} – {end_time}")
    print()

    # Eisenhower overview
    quadrants = categorize_eisenhower(tasks)
    print("## 🎯 Priority Overview (Eisenhower Matrix)")
    print()
    for quadrant, items in quadrants.items():
        if items:
            print(f"### {quadrant}")
            for item in items:
                print(f"- {item}")
            print()

    # Time-blocked schedule
    print("## ⏰ Time-Blocked Schedule")
    print()
    print("| Time | Duration | Task | Priority |")
    print("|------|----------|------|----------|")

    tasks_scheduled = 0
    for i, block in enumerate(task_blocks):
        # Insert break
        if num_breaks > 0 and tasks_scheduled > 0 and tasks_scheduled % break_interval == 0:
            break_end = current_time + timedelta(minutes=15)
            if break_end <= end:
                print(f"| {current_time.strftime('%H:%M')} | 15 min | ☕ **Break** | — |")
                current_time = break_end

        # Check if we have time
        task_end = current_time + timedelta(minutes=block["duration"])
        if task_end > end:
            print(f"| — | — | ⚠️ *{block['description']}* (overflow) | {PRIORITY_EMOJI.get(block['priority'], '⚪')} |")
            continue

        print(f"| {current_time.strftime('%H:%M')} | {block['duration']} min | {block['description']} | {PRIORITY_EMOJI.get(block['priority'], '⚪')} {block['priority']} |")
        current_time = task_end
        tasks_scheduled += 1

    # Buffer time
    if current_time < end:
        remaining = int((end - current_time).total_seconds() / 60)
        print(f"| {current_time.strftime('%H:%M')} | {remaining} min | 🔄 **Buffer / Review** | — |")

    print()
    print("## 📝 End-of-Day Checklist")
    print()
    print("- [ ] Review completed tasks")
    print("- [ ] Move unfinished tasks to tomorrow")
    print("- [ ] Note any blockers or dependencies")
    print("- [ ] Plan top 3 priorities for tomorrow")


def main():
    tasks = []
    start_time = "09:00"
    end_time = "18:00"
    num_breaks = 2

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--start" and i + 1 < len(sys.argv):
            start_time = sys.argv[i + 1]
            i += 2
        elif arg == "--end" and i + 1 < len(sys.argv):
            end_time = sys.argv[i + 1]
            i += 2
        elif arg == "--breaks" and i + 1 < len(sys.argv):
            num_breaks = int(sys.argv[i + 1])
            i += 2
        elif arg == "--from-tracker":
            tasks = load_tasks_from_tracker()
            i += 1
        elif arg == "--file" and i + 1 < len(sys.argv):
            tasks = load_tasks_from_file(sys.argv[i + 1])
            i += 2
        elif not arg.startswith("--"):
            tasks.append((arg, "medium"))
            i += 1
        else:
            i += 1

    if not tasks:
        print("❌ No tasks provided.")
        print(__doc__)
        sys.exit(1)

    generate_plan(tasks, start_time, end_time, num_breaks)


if __name__ == "__main__":
    main()
