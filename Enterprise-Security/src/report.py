import csv
from pathlib import Path


def generate_markdown_report(findings, severity_counts, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Enterprise Security Hardening Audit Report",
        "",
        "## Summary",
        "",
        f"- Total findings: {len(findings)}",
        f"- High severity: {severity_counts.get('HIGH', 0)}",
        f"- Medium severity: {severity_counts.get('MEDIUM', 0)}",
        f"- Low severity: {severity_counts.get('LOW', 0)}",
        "",
        "## Findings",
        "",
    ]

    if not findings:
        lines.append("No findings detected.")
    else:
        for index, finding in enumerate(findings, start=1):
            lines.extend([
                f"### Finding {index}: {finding['rule']}",
                "",
                f"- Severity: {finding['severity']}",
                f"- File: {finding['file']}",
                f"- Message: {finding['message']}",
                f"- Recommendation: {finding['recommendation']}",
                "",
            ])

    lines.extend([
        "## Defensive Value",
        "",
        "This audit helps identify insecure or weak network device configuration practices before they become operational or security risks.",
        "",
        "## Security Note",
        "",
        "This project uses sample configurations for educational and authorized lab environments only."
    ])

    output.write_text("\n".join(lines), encoding="utf-8")


def generate_csv_report(findings, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["severity", "file", "rule", "message", "recommendation"]

    with open(output, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(findings)
