# AGENTS.md — Butler Skill Instructions

> This file provides instructions for AI agents that read `AGENTS.md` (OpenAI Codex, OpenCode, and compatible platforms). For agents that read `SKILL.md` (Claude Code, GitHub Copilot, Gemini CLI, Cursor, Windsurf), see the companion `SKILL.md` file.

## Skills Available

### Butler — Personal Productivity Assistant

**Trigger:** When the user asks about task management, daily planning, email drafting, file organization, research & summarization, decision support, or workflow automation.

**Skill definition:** See [SKILL.md](./SKILL.md) for the full skill instructions, procedures, and tool references.

**Quick reference:**
- Task management → `python scripts/task-tracker.py`
- Daily planning → `python scripts/daily-planner.py`
- Decision analysis → `python scripts/decision-matrix.py`
- File organization → `bash scripts/project-organizer.sh`
- Summarization → `python scripts/summarizer.py`
- Email drafting → See `references/COMMUNICATION-GUIDE.md` and `assets/email-templates.md`
- Planning frameworks → See `references/PLANNING-STRATEGIES.md`
- Decision frameworks → See `references/DECISION-FRAMEWORKS.md`

## Important Rules

- **Never modify files without user approval** for file organization tasks.
- **Use structured output** — always use the templates in `assets/` for formatted output.
- **Be token-efficient** — load scripts and references only when needed.
- **Do NOT use butler for coding tasks** — it is only for productivity and organizational tasks.
