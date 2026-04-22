<p align="center">
  <h1 align="center">🎩 Butler</h1>
  <p align="center">
    <strong>Your AI-powered personal assistant — as an open-source Agent Skill.</strong>
  </p>
  <p align="center">
    <a href="https://agentskills.io">Agent Skills Standard</a> · 
    <a href="#installation">Install</a> · 
    <a href="#capabilities">Capabilities</a> · 
    <a href="#contributing">Contribute</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Agent_Skills-1.0-blue?style=flat-square" alt="Agent Skills 1.0">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
    <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square" alt="Python 3.10+">
  </p>
</p>

---

## What is Butler?

Butler is an **open-source [Agent Skill](https://agentskills.io)** that transforms any compatible AI coding agent into a personal productivity assistant. Just clone it into your project wnd your AI agent gets 7 new superpowers.

**Works with:** Claude Code · GitHub Copilot · Cursor · Windsurf · Gemini CLI · and any skills-compatible agent.

## Installation

### Quick Install (Any Platform)

```bash
# Clone directly into your project's skills directory
git clone https://github.com/tushar/butler.git .agents/skills/butler
```

### Platform-Specific Paths

| Platform | Install Path |
|----------|-------------|
| **GitHub Copilot** | `.agents/skills/butler/` |
| **Claude Code** | `.claude/skills/butler/` |
| **Gemini CLI** | `.gemini/skills/butler/` |
| **Cursor** | `.cursor/skills/butler/` |
| **Windsurf** | `.windsurf/skills/butler/` |

### Global Install (Available in All Projects)

```bash
# For Claude Code (global)
git clone https://github.com/tushar/butler.git ~/.claude/skills/butler

# For Gemini CLI (global)
git clone https://github.com/tushar/butler.git ~/.gemini/skills/butler
```

### Verify Installation

In your AI agent, type:
```
/skills
```
You should see `butler` in the list. Then try:
```
Help me plan my day
```

## Capabilities

### 1. 📋 Task Management
Manage to-do lists with priorities, deadlines, and progress tracking.

```
"Add a high-priority task: finish the API documentation by Friday"
"Show me all my pending tasks"
"Mark T003 as done"
```

### 2. 📅 Daily Planning
Generate structured daily plans with time blocks and the Eisenhower Matrix.

```
"Plan my day — I have 5 tasks to get through"
"Create a schedule for my workday starting at 10am"
```

### 3. ✉️ Email & Communication Drafting
Draft professional emails, messages, and reports with the right tone.

```
"Draft a follow-up email to the design team about the launch"
"Write a professional decline message for the vendor proposal"
```

### 4. 📁 File & Project Organization
Analyze and organize project files by type, date, or purpose.

```
"Analyze the files in this directory"
"Organize my downloads folder by file type"
```

### 5. 🔍 Research & Summarization
Summarize documents and compile structured research reports.

```
"Summarize this README file"
"Give me an executive summary of the project documentation"
```

### 6. 🎯 Decision Support
Build weighted decision matrices with recommendations.

```
"Help me decide between React, Vue, and Svelte for our frontend"
"Create a decision matrix for choosing a cloud provider"
```

### 7. ⚡ Routine Automation
Automate repetitive multi-step workflows.

```
"I do the same 5 steps every morning — help me automate this"
"Create a reusable workflow for our release process"
```

## Project Structure

```
butler/
├── SKILL.md                    # Core skill (Agent Skills format)
├── scripts/
│   ├── task-tracker.py         # Task management CLI
│   ├── daily-planner.py        # Daily plan generator
│   ├── decision-matrix.py      # Decision matrix builder
│   ├── project-organizer.sh    # File organizer
│   └── summarizer.py           # Text summarizer
├── references/
│   ├── COMMUNICATION-GUIDE.md  # Email & messaging rules
│   ├── PLANNING-STRATEGIES.md  # Time management frameworks
│   ├── RESEARCH-METHODOLOGY.md # Research procedures
│   └── DECISION-FRAMEWORKS.md  # Decision-making frameworks
├── assets/
│   ├── daily-plan-template.md
│   ├── task-list-template.md
│   ├── email-templates.md
│   ├── meeting-notes-template.md
│   ├── decision-matrix-template.md
│   └── weekly-review-template.md
├── README.md
├── LICENSE
└── .gitignore
```

## How It Works

Butler follows the **[Agent Skills](https://agentskills.io) open standard**:

1. **Discovery**: When your AI agent starts, it reads Butler's `name` and `description` from the YAML frontmatter (~100 tokens).
2. **Activation**: When you ask a productivity-related question, the agent matches it to Butler's description and loads the full skill instructions.
3. **Execution**: The agent follows Butler's step-by-step procedures, using the bundled scripts for deterministic tasks and reference docs for deep knowledge.
4. **Progressive Disclosure**: Scripts, references, and assets are only loaded when needed — keeping your context window efficient.

## Using Scripts Standalone

Butler's scripts also work as standalone CLI tools:

```bash
# Task management
python butler/scripts/task-tracker.py init
python butler/scripts/task-tracker.py add "Write documentation" --priority high --due 2026-04-25
python butler/scripts/task-tracker.py list

# Daily planning
python butler/scripts/daily-planner.py "Code review" "Team standup" "Write tests" --start 09:00

# Decision matrix
python butler/scripts/decision-matrix.py --options "React,Vue,Svelte" --criteria "Performance,Ecosystem,Learning Curve" --weights "0.4,0.3,0.3"

# File organization
bash butler/scripts/project-organizer.sh ./my-project --analyze

# Summarization
python butler/scripts/summarizer.py README.md --format executive
```

## Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. **Create a branch**: `git checkout -b feature/my-improvement`
3. **Make changes** following the [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
4. **Test** your changes with at least one AI agent
5. **Submit a PR** with a clear description of what changed and why

### Contribution Ideas
- 🌍 **Localization**: Add templates in other languages
- 🔧 **New scripts**: Additional productivity tools
- 📚 **Reference docs**: More frameworks and methodologies
- 🧪 **Test cases**: Evaluation prompts for skill quality

## License

MIT — see [LICENSE](LICENSE) for details.

---

<p align="center">
  Built with ❤️ as part of the <a href="https://github.com/tushar/AI-Agent-Disruptive-Skills">AI-Agent-Disruptive-Skills</a> project.
</p>
