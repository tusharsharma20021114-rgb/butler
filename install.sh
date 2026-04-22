#!/bin/bash
# ┌─────────────────────────────────────────────┐
# │  🎩 Butler — Universal Agent Skill Installer │
# └─────────────────────────────────────────────┘
#
# Automatically detects your AI coding agent and installs butler
# to the correct skills directory. Supports:
#   - Claude Code      (.claude/skills/)
#   - OpenCode         (.opencode/skills/)
#   - OpenAI Codex     (.codex/skills/ + AGENTS.md)
#   - GitHub Copilot   (.agents/skills/)
#   - Gemini CLI       (.gemini/skills/)
#   - Cursor           (.cursor/skills/)
#   - Windsurf         (.windsurf/skills/)
#
# Usage:
#   bash install.sh                    # Auto-detect and install locally
#   bash install.sh --global           # Install globally (all projects)
#   bash install.sh --platform claude  # Force a specific platform
#   bash install.sh --all              # Install for ALL platforms at once

set -euo pipefail

REPO_URL="https://github.com/tushar/butler.git"
SKILL_NAME="butler"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# ─────────────────────────────────────────────
# Platform Definitions
# ─────────────────────────────────────────────
declare -A LOCAL_PATHS
LOCAL_PATHS=(
    ["claude"]=".claude/skills"
    ["opencode"]=".opencode/skills"
    ["codex"]=".agents/skills"
    ["copilot"]=".agents/skills"
    ["gemini"]=".gemini/skills"
    ["cursor"]=".cursor/skills"
    ["windsurf"]=".windsurf/skills"
)

declare -A GLOBAL_PATHS
GLOBAL_PATHS=(
    ["claude"]="$HOME/.claude/skills"
    ["opencode"]="$HOME/.config/opencode/skills"
    ["codex"]="$HOME/.codex/skills"
    ["copilot"]="$HOME/.agents/skills"
    ["gemini"]="$HOME/.gemini/skills"
    ["cursor"]="$HOME/.cursor/skills"
    ["windsurf"]="$HOME/.windsurf/skills"
)

declare -A PLATFORM_NAMES
PLATFORM_NAMES=(
    ["claude"]="Claude Code"
    ["opencode"]="OpenCode"
    ["codex"]="OpenAI Codex"
    ["copilot"]="GitHub Copilot"
    ["gemini"]="Gemini CLI"
    ["cursor"]="Cursor"
    ["windsurf"]="Windsurf"
)

# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────
print_banner() {
    echo -e "${CYAN}"
    echo "  ┌─────────────────────────────────┐"
    echo "  │     🎩 Butler Skill Installer    │"
    echo "  │     Universal Agent Skill v1.0   │"
    echo "  └─────────────────────────────────┘"
    echo -e "${NC}"
}

detect_platforms() {
    local detected=()

    # Check for platform config directories
    [[ -d ".claude" ]] || command -v claude &>/dev/null && detected+=("claude")
    [[ -d ".opencode" ]] || command -v opencode &>/dev/null && detected+=("opencode")
    command -v codex &>/dev/null && detected+=("codex")
    [[ -d ".agents" ]] && detected+=("copilot")
    [[ -d ".gemini" ]] || command -v gemini &>/dev/null && detected+=("gemini")
    [[ -d ".cursor" ]] && detected+=("cursor")
    [[ -d ".windsurf" ]] && detected+=("windsurf")

    # If nothing detected, default to .agents (most universal)
    if [[ ${#detected[@]} -eq 0 ]]; then
        detected+=("copilot")
    fi

    echo "${detected[@]}"
}

install_skill() {
    local platform="$1"
    local target_dir="$2"
    local skill_dir="${target_dir}/${SKILL_NAME}"
    local platform_name="${PLATFORM_NAMES[$platform]:-$platform}"

    echo -e "  ${BLUE}→${NC} Installing for ${BOLD}${platform_name}${NC}..."
    echo -e "    Path: ${CYAN}${skill_dir}${NC}"

    # Create parent directory
    mkdir -p "$target_dir"

    # Check if already installed
    if [[ -d "$skill_dir" ]]; then
        echo -e "    ${YELLOW}⚠ Already installed. Updating...${NC}"
        rm -rf "$skill_dir"
    fi

    # Determine install method: copy local or clone from git
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    if [[ -f "${SCRIPT_DIR}/SKILL.md" ]]; then
        # We're running from the butler repo — copy directly
        # Use a temp dir to avoid "cannot copy into itself" errors
        local tmp_copy
        tmp_copy=$(mktemp -d)
        cp -r "$SCRIPT_DIR"/* "$tmp_copy/" 2>/dev/null || true
        cp -r "$SCRIPT_DIR"/.gitignore "$tmp_copy/" 2>/dev/null || true
        # Remove git artifacts and installer from the copy
        rm -rf "${tmp_copy}/.git" "${tmp_copy}/install.sh"
        # Remove any nested platform dirs that might exist from previous test installs
        rm -rf "${tmp_copy}/.claude" "${tmp_copy}/.opencode" "${tmp_copy}/.agents" "${tmp_copy}/.gemini" "${tmp_copy}/.cursor" "${tmp_copy}/.windsurf" "${tmp_copy}/.codex"
        # Move to target
        mv "$tmp_copy" "$skill_dir"
        echo -e "    ${GREEN}✅ Installed (copied from local)${NC}"
    else
        # Clone from GitHub
        git clone --quiet "$REPO_URL" "$skill_dir" 2>/dev/null
        rm -rf "${skill_dir}/.git" "${skill_dir}/install.sh"
        echo -e "    ${GREEN}✅ Installed (cloned from GitHub)${NC}"
    fi

    # For Codex: also create AGENTS.md reference if it doesn't exist
    if [[ "$platform" == "codex" ]]; then
        setup_codex_agents_md
    fi
}

setup_codex_agents_md() {
    local agents_file="AGENTS.md"

    if [[ -f "$agents_file" ]]; then
        # Check if butler section already exists
        if grep -q "butler" "$agents_file" 2>/dev/null; then
            echo -e "    ${YELLOW}ℹ AGENTS.md already references butler${NC}"
            return
        fi
        # Append butler reference
        echo "" >> "$agents_file"
        echo "## Butler Skill" >> "$agents_file"
        echo "This project uses the [butler](.agents/skills/butler/SKILL.md) skill for productivity tasks." >> "$agents_file"
        echo "When asked about task management, planning, email drafting, or decision making, load the butler skill." >> "$agents_file"
        echo -e "    ${GREEN}✅ Appended butler reference to AGENTS.md${NC}"
    else
        # Create minimal AGENTS.md
        cat > "$agents_file" <<'AGENTSEOF'
# AGENTS.md

## Skills

### Butler
This project uses the [butler](.agents/skills/butler/SKILL.md) skill for personal productivity tasks.
When the user asks about task management, daily planning, email drafting, file organization,
research summarization, decision making, or workflow automation, load and follow the butler skill instructions.

See `.agents/skills/butler/SKILL.md` for the full skill definition.
AGENTSEOF
        echo -e "    ${GREEN}✅ Created AGENTS.md with butler reference${NC}"
    fi
}

# ─────────────────────────────────────────────
# Main Logic
# ─────────────────────────────────────────────
print_banner

MODE="local"
PLATFORM=""
ALL_PLATFORMS=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --global)
            MODE="global"
            shift
            ;;
        --platform)
            PLATFORM="$2"
            shift 2
            ;;
        --all)
            ALL_PLATFORMS=true
            shift
            ;;
        --help|-h)
            echo "Usage: bash install.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --global            Install globally (all projects)"
            echo "  --platform NAME     Install for specific platform"
            echo "                      (claude|opencode|codex|copilot|gemini|cursor|windsurf)"
            echo "  --all               Install for ALL platforms"
            echo "  -h, --help          Show this help"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Determine platforms to install for
if [[ "$ALL_PLATFORMS" == true ]]; then
    PLATFORMS=("claude" "opencode" "codex" "copilot" "gemini" "cursor" "windsurf")
    echo -e "  ${BOLD}Mode:${NC} Installing for ALL platforms"
elif [[ -n "$PLATFORM" ]]; then
    PLATFORMS=("$PLATFORM")
    echo -e "  ${BOLD}Mode:${NC} Installing for ${PLATFORM_NAMES[$PLATFORM]:-$PLATFORM}"
else
    read -ra PLATFORMS <<< "$(detect_platforms)"
    echo -e "  ${BOLD}Mode:${NC} Auto-detected platforms"
fi

echo -e "  ${BOLD}Scope:${NC} ${MODE}"
echo ""

# Install for each platform
INSTALLED=0
for platform in "${PLATFORMS[@]}"; do
    if [[ "$MODE" == "global" ]]; then
        target="${GLOBAL_PATHS[$platform]:-}"
    else
        target="${LOCAL_PATHS[$platform]:-}"
    fi

    if [[ -n "$target" ]]; then
        install_skill "$platform" "$target"
        INSTALLED=$((INSTALLED + 1))
    fi
done

echo ""
echo -e "${GREEN}${BOLD}🎩 Butler installed for ${INSTALLED} platform(s)!${NC}"
echo ""
echo -e "  ${BOLD}Verify:${NC} Open your AI agent and type: ${CYAN}/skills${NC}"
echo -e "  ${BOLD}Try it:${NC} Ask your agent: ${CYAN}\"Help me plan my day\"${NC}"
echo ""
