#!/bin/bash
# Butler Project Organizer — Analyze and organize files in a directory.
#
# Usage:
#   bash project-organizer.sh [directory] [--analyze | --organize | --dry-run]
#
# Options:
#   --analyze   Show current file distribution without making changes
#   --organize  Actually move files into organized structure
#   --dry-run   Show what would happen without making changes (default)

set -euo pipefail

TARGET_DIR="${1:-.}"
ACTION="${2:---dry-run}"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# File type categories
declare -A CATEGORIES
CATEGORIES=(
    ["documents"]="pdf doc docx txt md rst tex odt rtf"
    ["images"]="jpg jpeg png gif svg bmp ico webp tiff"
    ["code"]="py js ts jsx tsx go rs java c cpp h hpp cs rb php swift kt"
    ["data"]="json csv xml yaml yml toml ini cfg conf"
    ["media"]="mp4 mp3 wav avi mkv mov flac ogg webm"
    ["archives"]="zip tar gz bz2 xz 7z rar"
    ["notebooks"]="ipynb"
    ["scripts"]="sh bash zsh fish bat ps1 cmd"
)

get_category() {
    local ext="${1##*.}"
    ext="${ext,,}"  # lowercase

    for category in "${!CATEGORIES[@]}"; do
        for file_ext in ${CATEGORIES[$category]}; do
            if [[ "$ext" == "$file_ext" ]]; then
                echo "$category"
                return
            fi
        done
    done
    echo "other"
}

analyze() {
    echo -e "${CYAN}📊 Butler Project Analyzer${NC}"
    echo "═══════════════════════════════════════"
    echo -e "Target: ${BLUE}${TARGET_DIR}${NC}"
    echo ""

    local total=0
    declare -A counts
    declare -A sizes

    while IFS= read -r -d '' file; do
        if [[ -f "$file" ]]; then
            category=$(get_category "$file")
            counts[$category]=$(( ${counts[$category]:-0} + 1 ))
            file_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo 0)
            sizes[$category]=$(( ${sizes[$category]:-0} + file_size ))
            total=$((total + 1))
        fi
    done < <(find "$TARGET_DIR" -maxdepth 3 -not -path '*/\.*' -print0)

    echo -e "${GREEN}File Distribution:${NC}"
    echo "───────────────────────────────────────"
    printf "%-15s | %5s | %10s\n" "Category" "Count" "Size"
    echo "───────────────────────────────────────"

    for category in $(echo "${!counts[@]}" | tr ' ' '\n' | sort); do
        count=${counts[$category]}
        size=${sizes[$category]}
        # Human-readable size
        if (( size > 1073741824 )); then
            hr_size="$(echo "scale=1; $size/1073741824" | bc)G"
        elif (( size > 1048576 )); then
            hr_size="$(echo "scale=1; $size/1048576" | bc)M"
        elif (( size > 1024 )); then
            hr_size="$(echo "scale=1; $size/1024" | bc)K"
        else
            hr_size="${size}B"
        fi
        printf "%-15s | %5d | %10s\n" "$category" "$count" "$hr_size"
    done

    echo "───────────────────────────────────────"
    echo -e "Total files: ${YELLOW}${total}${NC}"
}

dry_run() {
    echo -e "${YELLOW}🔍 Butler Organizer — Dry Run${NC}"
    echo "═══════════════════════════════════════"
    echo -e "Target: ${BLUE}${TARGET_DIR}${NC}"
    echo ""
    echo "Proposed changes (no files will be moved):"
    echo ""

    while IFS= read -r -d '' file; do
        if [[ -f "$file" ]]; then
            category=$(get_category "$file")
            basename=$(basename "$file")
            echo -e "  ${basename} → ${GREEN}${category}/${basename}${NC}"
        fi
    done < <(find "$TARGET_DIR" -maxdepth 1 -not -path '*/\.*' -not -name '.*' -print0)

    echo ""
    echo -e "${CYAN}Run with --organize to apply these changes.${NC}"
}

organize() {
    echo -e "${GREEN}📁 Butler Organizer — Organizing files${NC}"
    echo "═══════════════════════════════════════"

    local moved=0
    local log_file="${TARGET_DIR}/butler-organize-log.txt"

    echo "# Butler Organization Log — $(date)" > "$log_file"
    echo "# Original Path → New Path" >> "$log_file"

    while IFS= read -r -d '' file; do
        if [[ -f "$file" ]]; then
            category=$(get_category "$file")
            dest_dir="${TARGET_DIR}/${category}"
            basename=$(basename "$file")

            mkdir -p "$dest_dir"

            if [[ "$file" != "${dest_dir}/${basename}" ]]; then
                mv "$file" "${dest_dir}/${basename}"
                echo "${file} → ${dest_dir}/${basename}" >> "$log_file"
                echo -e "  ✅ ${basename} → ${GREEN}${category}/${NC}"
                moved=$((moved + 1))
            fi
        fi
    done < <(find "$TARGET_DIR" -maxdepth 1 -type f -not -name '.*' -not -name 'butler-*' -print0)

    echo ""
    echo -e "Moved ${YELLOW}${moved}${NC} files."
    echo -e "Log saved to: ${BLUE}${log_file}${NC}"
    echo -e "${CYAN}To undo, use the log file to reverse the moves.${NC}"
}

case "$ACTION" in
    --analyze)
        analyze
        ;;
    --organize)
        organize
        ;;
    --dry-run)
        dry_run
        ;;
    *)
        echo "Usage: bash project-organizer.sh [directory] [--analyze | --organize | --dry-run]"
        exit 1
        ;;
esac
