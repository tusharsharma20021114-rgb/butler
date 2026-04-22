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
    <img src="https://img.shields.io/badge/Agent_Skills-1.1-blue?style=flat-square" alt="Agent Skills 1.1">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
    <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/Platforms-7-purple?style=flat-square" alt="7 Platforms">
  </p>
</p>

---

## What is Butler?

Butler is an **open-source [Agent Skill](https://agentskills.io)** that transforms any compatible AI coding agent into a personal productivity assistant. Just clone it into your project and your AI agent gets 7 new superpowers.

**Works with:** Claude Code · OpenCode · OpenAI Codex · GitHub Copilot · Gemini CLI · Cursor · Windsurf

## Installation

### 🚀 One-Line Install (Auto-Detect)

```bash
curl -fsSL https://raw.githubusercontent.com/tushar/butler/main/install.sh | bash
```

Or clone and run:
```bash
git clone https://github.com/tushar/butler.git /tmp/butler-install
bash /tmp/butler-install/install.sh
```

The installer **auto-detects** which AI agents you have and installs butler to the right directory.

### 📋 Platform-Specific Install

<table>
<tr>
<th>Platform</th>
<th>Local (Project)</th>
<th>Global (All Projects)</th>
</tr>
<tr>
<td><strong>Claude Code</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .claude/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.claude/skills/butler
```
</td>
</tr>
<tr>
<td><strong>OpenCode</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .opencode/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.config/opencode/skills/butler
```
</td>
</tr>
<tr>
<td><strong>OpenAI Codex</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .agents/skills/butler
```
> Also create an `AGENTS.md` — see [Codex Setup](#codex-setup) below.
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.codex/skills/butler
```
</td>
</tr>
<tr>
<td><strong>GitHub Copilot</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .agents/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.agents/skills/butler
```
</td>
</tr>
<tr>
<td><strong>Gemini CLI</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .gemini/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.gemini/skills/butler
```
</td>
</tr>
<tr>
<td><strong>Cursor</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .cursor/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.cursor/skills/butler
```
</td>
</tr>
<tr>
<td><strong>Windsurf</strong></td>
<td>

```bash
git clone https://github.com/tushar/butler.git .windsurf/skills/butler
```
</td>
<td>

```bash
git clone https://github.com/tushar/butler.git ~/.windsurf/skills/butler
```
</td>
</tr>
</table>

### 🔥 Install for ALL Platforms at Once

```bash
bash install.sh --all
```

### Codex Setup

OpenAI Codex uses `AGENTS.md` to discover skills. After installing butler, create or update your project's `AGENTS.md`:

```markdown
# AGENTS.md

## Skills

### Butler
This project uses the [butler](.agents/skills/butler/SKILL.md) skill for personal productivity tasks.
When the user asks about task management, daily planning, email drafting, file organization,
research summarization, decision making, or workflow automation, load and follow the butler skill.
```

> **Tip:** The `install.sh --platform codex` command does this automatically.

### Verify Installation

In your AI agent, type:
```
/skills
```
You should see `butler` listed. Then try:
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

## Platform Compatibility

| Feature | Claude Code | OpenCode | Codex | Copilot | Gemini CLI | Cursor | Windsurf |
|---------|:---------:|:--------:|:-----:|:-------:|:----------:|:------:|:--------:|
| SKILL.md Discovery | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Progressive Disclosure | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Script Execution | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reference Loading | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AGENTS.md Support | — | ✅ | ✅ | — | — | — | — |
| Global Install | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Project Structure

```
butler/
├── SKILL.md                    # Core skill (Agent Skills format)
├── AGENTS.md                   # Codex/OpenCode compatibility
├── install.sh                  # Universal auto-installer
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

> **Codex/OpenCode Bonus**: These platforms also read `AGENTS.md`, which provides an additional activation path for butler. The installer creates this file automatically.

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
- 🔌 **Platform support**: Improve compatibility with new agents

## License

MIT — see [LICENSE](LICENSE) for details.

---

<p align="center">
  Built with ❤️ as part of the <a href="https://github.com/tushar/AI-Agent-Disruptive-Skills">AI-Agent-Disruptive-Skills</a> project.
</p>
