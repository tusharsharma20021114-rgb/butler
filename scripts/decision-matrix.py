#!/usr/bin/env python3
"""
Butler Decision Matrix — Generate weighted decision matrices.

Usage:
    python decision-matrix.py interactive               # Interactive mode
    python decision-matrix.py --options "A,B,C" --criteria "Cost,Speed,Quality" --weights "0.4,0.3,0.3"

Options:
    --options     Comma-separated list of options to evaluate
    --criteria    Comma-separated list of evaluation criteria
    --weights     Comma-separated weights for criteria (must sum to 1.0)
    --scores      JSON string of scores: '{"A": [8,7,9], "B": [6,9,7]}'
"""

import sys
import json


def normalize_weights(weights):
    """Normalize weights to sum to 1.0."""
    total = sum(weights)
    if total == 0:
        return [1.0 / len(weights)] * len(weights)
    return [w / total for w in weights]


def calculate_matrix(options, criteria, weights, scores):
    """Calculate weighted scores for each option."""
    results = {}
    for option in options:
        option_scores = scores.get(option, [5] * len(criteria))
        weighted = sum(s * w for s, w in zip(option_scores, weights))
        results[option] = {
            "raw_scores": option_scores,
            "weighted_score": round(weighted, 2),
        }
    return results


def print_matrix(options, criteria, weights, scores, results):
    """Print a formatted decision matrix."""
    print("# 🎯 Decision Matrix Analysis")
    print()

    # Criteria and weights table
    print("## Evaluation Criteria")
    print()
    print("| Criteria | Weight | Importance |")
    print("|----------|--------|------------|")
    for c, w in zip(criteria, weights):
        bar_len = int(w * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"| {c} | {w:.0%} | {bar} |")
    print()

    # Full matrix
    print("## Score Matrix (1-10 scale)")
    print()
    header = "| Option |" + "|".join(f" {c} " for c in criteria) + "| **Weighted Total** |"
    separator = "|--------|" + "|".join("-------" for _ in criteria) + "|-------------------|"
    print(header)
    print(separator)

    for option in options:
        r = results[option]
        scores_str = "|".join(f" {s}/10 " for s in r["raw_scores"])
        print(f"| **{option}** |{scores_str}| **{r['weighted_score']:.2f}** |")
    print()

    # Ranking
    ranked = sorted(results.items(), key=lambda x: x[1]["weighted_score"], reverse=True)
    print("## 🏆 Ranking")
    print()
    medals = ["🥇", "🥈", "🥉"]
    for i, (option, data) in enumerate(ranked):
        medal = medals[i] if i < len(medals) else f"#{i+1}"
        print(f"{medal} **{option}** — Score: {data['weighted_score']:.2f}")
    print()

    # Recommendation
    winner = ranked[0]
    runner_up = ranked[1] if len(ranked) > 1 else None
    print("## 💡 Recommendation")
    print()
    print(f"**{winner[0]}** is the recommended choice with a weighted score of **{winner[1]['weighted_score']:.2f}**.")
    if runner_up:
        gap = winner[1]["weighted_score"] - runner_up[1]["weighted_score"]
        if gap < 0.5:
            print(f"\n> ⚠️ Note: The margin over **{runner_up[0]}** ({runner_up[1]['weighted_score']:.2f}) is narrow ({gap:.2f} points). Consider qualitative factors before deciding.")
        else:
            print(f"\n> ✅ Clear advantage over **{runner_up[0]}** ({runner_up[1]['weighted_score']:.2f}) by {gap:.2f} points.")

    # Sensitivity note
    print()
    print("## 📊 Sensitivity Notes")
    print()
    print("- Scores are subjective estimates. Consider adjusting weights if priorities shift.")
    print("- A small change in weights can flip close results — test with different weight distributions.")
    print("- This matrix evaluates *quantifiable* criteria. Don't forget gut feeling and intangibles.")


def interactive_mode():
    """Run in interactive mode, prompting for input."""
    print("🎯 Butler Decision Matrix — Interactive Mode")
    print("=" * 45)
    print()

    options_str = input("Enter options (comma-separated): ").strip()
    options = [o.strip() for o in options_str.split(",")]

    criteria_str = input("Enter criteria (comma-separated): ").strip()
    criteria = [c.strip() for c in criteria_str.split(",")]

    weights_str = input(f"Enter weights for {len(criteria)} criteria (comma-separated, will be normalized): ").strip()
    weights = normalize_weights([float(w) for w in weights_str.split(",")])

    scores = {}
    for option in options:
        print(f"\nScore '{option}' on each criterion (1-10):")
        option_scores = []
        for criterion in criteria:
            score = int(input(f"  {criterion}: ").strip())
            option_scores.append(min(10, max(1, score)))
        scores[option] = option_scores

    print("\n")
    results = calculate_matrix(options, criteria, weights, scores)
    print_matrix(options, criteria, weights, scores, results)


def cli_mode(args):
    """Run from command-line arguments."""
    options = []
    criteria = []
    weights = []
    scores = {}

    i = 0
    while i < len(args):
        if args[i] == "--options" and i + 1 < len(args):
            options = [o.strip() for o in args[i + 1].split(",")]
            i += 2
        elif args[i] == "--criteria" and i + 1 < len(args):
            criteria = [c.strip() for c in args[i + 1].split(",")]
            i += 2
        elif args[i] == "--weights" and i + 1 < len(args):
            weights = [float(w) for w in args[i + 1].split(",")]
            i += 2
        elif args[i] == "--scores" and i + 1 < len(args):
            scores = json.loads(args[i + 1])
            i += 2
        else:
            i += 1

    if not options or not criteria:
        print("❌ --options and --criteria are required.")
        print(__doc__)
        sys.exit(1)

    if not weights:
        weights = [1.0 / len(criteria)] * len(criteria)
    weights = normalize_weights(weights)

    # If no scores provided, use defaults
    if not scores:
        print("⚠️ No scores provided. Using default score of 5 for all.")
        scores = {opt: [5] * len(criteria) for opt in options}

    results = calculate_matrix(options, criteria, weights, scores)
    print_matrix(options, criteria, weights, scores, results)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "interactive":
        interactive_mode()
    else:
        cli_mode(sys.argv[1:])


if __name__ == "__main__":
    main()
