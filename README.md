<p align="center">
  <h1 align="center">🎩 Butler</h1>
  <p align="center">
    <strong>Open-Source AI Agent Skill — Turn any AI coding assistant into your personal productivity butler.</strong>
  </p>
  <p align="center">
    <a href="https://agentskills.io">Agent Skills Standard</a> · 
    <a href="#-quick-start">Quick Start</a> · 
    <a href="#-what-can-butler-do">Capabilities</a> · 
    <a href="#-why-butler">Why Butler</a> · 
    <a href="#-contributing">Contribute</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Agent_Skills-v1.1-blue?style=flat-square" alt="Agent Skills v1.1">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
    <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/Platforms-7-purple?style=flat-square" alt="7 Platforms Supported">
  </p>
</p>

---

## 🤔 What is Butler?

**Butler** is an open-source **AI Agent Skill** that gives your AI coding assistant (Claude Code, OpenCode, Codex, Copilot, etc.) the ability to act as a **personal productivity assistant**. Think of it as a plugin that teaches your AI agent how to manage tasks, plan your day, draft emails, make decisions, and more — all without leaving your terminal.

It follows the [Agent Skills](https://agentskills.io) open standard — the universal format for packaging reusable AI agent capabilities. One `git clone` and your AI agent learns 7 new skills.

### How it works (in 30 seconds)

```
1. You clone butler into your project's skills folder
2. Your AI agent auto-discovers it on startup (reads ~100 tokens of metadata)
3. When you ask "help me plan my day" → the agent loads butler's full instructions
4. Butler's procedures guide the agent to use bundled scripts & templates
5. You get structured, professional outputs — not generic chat responses
```

---

## 💡 Why Butler?

### The Problem
AI coding agents are great at writing code, but when you ask them to:
- "Track my project tasks" → they give you a generic markdown list that disappears next session
- "Plan my day" → they write a paragraph with no structure or time awareness  
- "Help me decide between X and Y" → they give opinions, not analysis

### The Solution
Butler provides **structured procedures**, **executable scripts**, and **professional templates** that turn vague requests into precise, repeatable, high-quality outputs.

### Measured Impact

We built a complex project (696-line CLI app) **with** and **without** butler, and scored the results:

| Metric | WITH Butler | WITHOUT Butler | Improvement |
|--------|:-----------:|:--------------:|:-----------:|
| **Overall Score** | **91/100** | **62/100** | **+47%** |
| Progress Visibility | 10/10 | 2/10 | +8 points |
| Task Management | 10/10 | 3/10 | +7 points |
| Decision Making | 9/10 | 4/10 | +5 points |
| Feature Completeness | 10/10 | 6/10 | +4 points |
| Planning Quality | 9/10 | 5/10 | +4 points |

> **Key insight:** Butler doesn't write code for you — it structures the *process* around your code. The 47% improvement comes from better planning, tracking, decision-making, and documentation.

---

## 🚀 Quick Start

### One-Line Install (Auto-Detects Your Platform)

```bash
git clone https://github.com/tusharsharma20021114-rgb/butler.git /tmp/butler && bash /tmp/butler/install.sh
```

The installer auto-detects which AI agents you have installed and copies butler to the correct directory.

### Manual Install (Pick Your Platform)

Clone butler into your AI agent's skills directory:

| Platform | Command |
|----------|---------|
| **Claude Code** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .claude/skills/butler` |
| **OpenCode** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .opencode/skills/butler` |
| **OpenAI Codex** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .agents/skills/butler` |
| **GitHub Copilot** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .agents/skills/butler` |
| **Gemini CLI** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .gemini/skills/butler` |
| **Cursor** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .cursor/skills/butler` |
| **Windsurf** | `git clone https://github.com/tusharsharma20021114-rgb/butler.git .windsurf/skills/butler` |

### Global Install (Available in ALL Your Projects)

```bash
# Claude Code
git clone https://github.com/tusharsharma20021114-rgb/butler.git ~/.claude/skills/butler

# OpenCode
git clone https://github.com/tusharsharma20021114-rgb/butler.git ~/.config/opencode/skills/butler

# OpenAI Codex
git clone https://github.com/tusharsharma20021114-rgb/butler.git ~/.codex/skills/butler

# Gemini CLI
git clone https://github.com/tusharsharma20021114-rgb/butler.git ~/.gemini/skills/butler
```

### Install for ALL Platforms at Once

```bash
git clone https://github.com/tusharsharma20021114-rgb/butler.git /tmp/butler
bash /tmp/butler/install.sh --all
```

### Extra Step for OpenAI Codex

Codex uses `AGENTS.md` to discover skills. After installing, add this to your project's `AGENTS.md`:

```markdown
## Butler Skill
This project uses the [butler](.agents/skills/butler/SKILL.md) skill.
When asked about tasks, planning, emails, or decisions, load the butler skill.
```

> **Tip:** `bash install.sh --platform codex` creates this automatically.

### Verify Installation

Open your AI agent and type:
```
/skills
```
You should see `butler` listed. Then try asking:
```
Help me plan my day
```

---

## 🎯 What Can Butler Do?

### 1. 📋 Task Management
Persistent, prioritized task tracking with due dates, categories, and progress bars.

**Try saying:**
```
"Add a high-priority task: finish the API docs by Friday"
"Show my pending tasks"
"Mark T003 as done"
"Give me a task summary"
```

**What you get:**
```
🔴 HIGH PRIORITY
──────────────────────────────────────────────────
  ⬜ T001: Finish API documentation 📅 2026-04-25 [docs]
  ⬜ T002: Fix login bug 📅 2026-04-23 [code]

🟡 MEDIUM PRIORITY
──────────────────────────────────────────────────
  ⬜ T003: Review pull requests [code]

📊 Total: 3 | ✅ Done: 0 | ⬜ Pending: 3 | 🔥 Overdue: 0
Progress: [░░░░░░░░░░░░░░░░░░░░] 0%
```

**Powered by:** `scripts/task-tracker.py` — a full CLI tool that persists tasks to `butler-tasks.json`.

---

### 2. 📅 Daily Planning
Structured daily plans using the **Eisenhower Matrix** with time blocks, breaks, and overflow detection.

**Try saying:**
```
"Plan my day — I need to do code review, team standup, write tests, and draft a report"
"Create a schedule starting at 9am ending at 5pm with 2 breaks"
```

**What you get:**
```
# 📋 Daily Plan — Wednesday, April 22, 2026
Working hours: 09:00 – 17:00

## 🎯 Priority Overview (Eisenhower Matrix)

### 🔥 DO FIRST (Urgent + Important)
- Fix production bug

### 📅 SCHEDULE (Important, Not Urgent)
- Code review
- Write unit tests

## ⏰ Time-Blocked Schedule
| Time  | Duration | Task                  | Priority |
|-------|----------|-----------------------|----------|
| 09:00 | 90 min   | Fix production bug    | 🔴 high  |
| 10:30 | 15 min   | ☕ Break              | —        |
| 10:45 | 45 min   | Team standup          | 🟡 med   |
| 11:30 | 60 min   | Code review           | 🟡 med   |
| 12:30 | 60 min   | 🍽️ Lunch             | —        |
...
```

**Powered by:** `scripts/daily-planner.py` — integrates with the task tracker.

---

### 3. ✉️ Email & Communication Drafting
Professional emails with the right tone, structure, and length — using curated templates.

**Try saying:**
```
"Draft a follow-up email to the design team about the product launch"
"Write a professional message declining a vendor proposal"
"Help me write a status update for my manager"
```

Butler uses 6 email templates (intro, status update, thank you, request, apology, cold outreach) and a comprehensive tone guide (formal → casual → urgent).

**Powered by:** `references/COMMUNICATION-GUIDE.md` + `assets/email-templates.md`

---

### 4. 📁 File & Project Organization
Analyze your project's file distribution and organize files by category — with dry-run and undo support.

**Try saying:**
```
"Analyze the files in this directory"
"Organize my downloads folder by file type"
```

**What you get:**
```
📊 Butler Project Analyzer
═══════════════════════════════════════
Category        | Count |       Size
───────────────────────────────────────
code            |     4 |      29.5K
data            |     1 |       1.3K
documents       |    12 |      35.3K
───────────────────────────────────────
Total files: 19
```

**Powered by:** `scripts/project-organizer.sh` — supports `--analyze`, `--dry-run`, and `--organize` with rollback log.

---

### 5. 🔍 Research & Summarization
Summarize any document in 4 formats: bullet points, executive summary, detailed breakdown, or outline.

**Try saying:**
```
"Summarize this README"
"Give me an executive summary of the project docs"
"Create a detailed breakdown of this file"
```

**Output formats:**
- **bullet** — Key takeaways as bullet points
- **executive** — One-paragraph summary
- **detailed** — Section-by-section analysis with word counts
- **outline** — Hierarchical outline

**Powered by:** `scripts/summarizer.py` + `references/RESEARCH-METHODOLOGY.md`

---

### 6. 🎯 Decision Support
Weighted decision matrices with rankings, recommendations, and sensitivity analysis.

**Try saying:**
```
"Help me decide between React, Vue, and Svelte for our frontend"
"Create a decision matrix for choosing a cloud provider"
```

**What you get:**
```
## 🏆 Ranking
🥇 Python — Score: 8.40
🥈 Node — Score: 7.15
🥉 Rust — Score: 5.70

## 💡 Recommendation
Python is the recommended choice with a weighted score of 8.40.
✅ Clear advantage over Node (7.15) by 1.25 points.

## 📊 Sensitivity Notes
- A small change in weights can flip close results
```

**Powered by:** `scripts/decision-matrix.py` + `references/DECISION-FRAMEWORKS.md` (covers weighted matrix, SWOT, pros/cons, risk assessment, and the Two-Way Door test).

---

### 7. ⚡ Routine Automation
Turn repetitive multi-step workflows into reusable scripts.

**Try saying:**
```
"I do the same 5 steps every Monday morning — help me automate this"
"Create a reusable workflow for our release process"
```

Butler breaks workflows into discrete steps, creates a checklist, and offers to save it as a script.

---

## 🏗️ Project Structure

```
butler/
├── SKILL.md                        # 🧠 Core skill definition (Agent Skills format)
├── AGENTS.md                       # 🔌 Codex/OpenCode compatibility layer
├── install.sh                      # 🚀 Universal auto-installer
│
├── scripts/                        # ⚙️ Executable tools
│   ├── task-tracker.py             #    Task management CLI
│   ├── daily-planner.py            #    Daily plan generator with Eisenhower matrix
│   ├── decision-matrix.py          #    Weighted decision matrix builder
│   ├── project-organizer.sh        #    File organizer with dry-run & undo
│   └── summarizer.py               #    Multi-format text summarizer
│
├── references/                     # 📚 On-demand knowledge (loaded when needed)
│   ├── COMMUNICATION-GUIDE.md      #    Tone spectrum, email rules, common scenarios
│   ├── PLANNING-STRATEGIES.md      #    Eisenhower, Time Blocking, Pomodoro, GTD
│   ├── RESEARCH-METHODOLOGY.md     #    5-step research process, source evaluation
│   └── DECISION-FRAMEWORKS.md      #    SWOT, risk matrix, two-way door test
│
├── assets/                         # 📝 Structured output templates
│   ├── daily-plan-template.md
│   ├── task-list-template.md
│   ├── email-templates.md          #    6 professional email templates
│   ├── meeting-notes-template.md
│   ├── decision-matrix-template.md
│   └── weekly-review-template.md
│
├── README.md                       # This file
├── LICENSE                         # MIT
└── .gitignore
```

---

## 🔌 Platform Compatibility

Butler works across **7 AI coding platforms** — the most widely compatible agent skill available:

| Feature | Claude Code | OpenCode | Codex | Copilot | Gemini CLI | Cursor | Windsurf |
|---------|:---------:|:--------:|:-----:|:-------:|:----------:|:------:|:--------:|
| Auto-Discovery | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Script Execution | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reference Loading | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AGENTS.md Support | — | ✅ | ✅ | — | — | — | — |
| Global Install | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Installer Flags

```bash
bash install.sh                    # Auto-detect your platform
bash install.sh --platform claude  # Install for a specific platform
bash install.sh --all              # Install for ALL 7 platforms
bash install.sh --global           # Install globally (all projects)
```

---

## ⚙️ Using Scripts Standalone

Butler's scripts work independently as CLI tools — no AI agent required:

```bash
# ── Task Management ──
python scripts/task-tracker.py init
python scripts/task-tracker.py add "Write docs" --priority high --due 2026-04-25 --category work
python scripts/task-tracker.py list
python scripts/task-tracker.py done T001
python scripts/task-tracker.py summary

# ── Daily Planning ──
python scripts/daily-planner.py "Code review" "Team standup" "Write tests" --start 09:00 --end 17:00
python scripts/daily-planner.py --from-tracker   # Reads from butler-tasks.json

# ── Decision Matrix ──
python scripts/decision-matrix.py interactive     # Interactive mode
python scripts/decision-matrix.py \
  --options "React,Vue,Svelte" \
  --criteria "Speed,Ecosystem,Learning Curve" \
  --weights "0.4,0.3,0.3" \
  --scores '{"React": [7,9,5], "Vue": [8,7,8], "Svelte": [9,5,9]}'

# ── File Organization ──
bash scripts/project-organizer.sh ./my-project --analyze    # Analyze file distribution5
bash scripts/project-organizer.sh ./my-project --dry-run    # Preview changes
bash scripts/project-organizer.sh ./my-project --organize   # Apply (creates undo log)

# ── Summarization ──
python scripts/summarizer.py README.md --format bullet       # Bullet points
python scripts/summarizer.py README.md --format executive     # One paragraph
python scripts/summarizer.py README.md --format detailed      # Full breakdown
python scripts/summarizer.py README.md --format outline       # Hierarchical
python scripts/summarizer.py docs/ --recursive                # Summarize entire directory
```

---

## 🔍 How Butler Works Under the Hood

Butler follows the **[Agent Skills](https://agentskills.io)** open standard:

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Agent Startup                          │
│  Agent reads SKILL.md frontmatter (~100 tokens)             │
│  Stores: name="butler", description="personal assistant..." │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼  User asks: "Help me plan my day"
┌─────────────────────────────────────────────────────────────┐
│                    Skill Activation                          │
│  Agent matches request → butler's description               │
│  Loads full SKILL.md body (~4000 tokens)                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼  Butler procedures say: "Run daily-planner.py"
┌─────────────────────────────────────────────────────────────┐
│                    Script Execution                          │
│  Agent runs: python scripts/daily-planner.py --from-tracker │
│  References: PLANNING-STRATEGIES.md (if needed)             │
│  Templates: daily-plan-template.md                          │
└─────────────────────────────────────────────────────────────┘
```

**Key design principle: Progressive Disclosure**
- At startup: only ~100 tokens loaded (name + description)
- On activation: ~4000 tokens (full procedures)
- Scripts/references: loaded only when that specific capability is invoked
- Result: **minimal token usage**, maximum capability

---

## 🤝 Contributing

Contributions are welcome! Butler is designed to be modular — you can add new capabilities without touching existing ones.

### How to Contribute

1. **Fork** this repository
2. **Create a branch**: `git checkout -b feature/my-improvement`
3. **Make changes** — follow the file structure conventions
4. **Test** your changes with at least one AI agent
5. **Submit a PR** with a clear description

### Contribution Ideas

| Category | Ideas |
|----------|-------|
| 🌍 **Localization** | Templates in Hindi, Spanish, Chinese, etc. |
| 🔧 **New Scripts** | Time tracker, expense logger, habit tracker |
| 📚 **New References** | Agile methodology, negotiation frameworks |
| 📝 **New Templates** | Sprint retrospective, 1-on-1 meeting notes |
| 🧪 **Evaluation** | Benchmark prompts to measure skill quality |
| 🔌 **Platform Support** | Test & document on new AI agents |

### Adding a New Capability

1. Add the procedure to `SKILL.md` under a new `### N. Capability Name` section
2. Create any scripts in `scripts/`
3. Add templates to `assets/`
4. Add reference knowledge to `references/`
5. Update this README

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details. Use it, modify it, share it.

---

## ⭐ Star This Repo

If butler saved you time, give it a ⭐ — it helps others discover it.

---

<p align="center">
  <strong>🎩 Built to make AI agents actually useful for real work.</strong>
  <br>
  Part of the <a href="https://github.com/tusharsharma20021114-rgb/AI-Agent-Disruptive-Skills">AI-Agent-Disruptive-Skills</a> project.
</p>
