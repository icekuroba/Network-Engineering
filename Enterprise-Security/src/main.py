from auditor import audit_multiple_configs, count_by_severity
from report import generate_markdown_report, generate_csv_report


CONFIG_FILES = [
    "data/sample_router_config.txt",
    "data/sample_switch_config.txt",
]

MARKDOWN_REPORT = "reports/hardening-audit-report.md"
CSV_REPORT = "reports/hardening-audit-findings.csv"


def main():
    findings = audit_multiple_configs(CONFIG_FILES)
    severity_counts = count_by_severity(findings)

    generate_markdown_report(findings, severity_counts, MARKDOWN_REPORT)
    generate_csv_report(findings, CSV_REPORT)

    print("Enterprise Security Hardening Auditor completed.")
    print(f"Configuration files analyzed: {len(CONFIG_FILES)}")
    print(f"Findings detected: {len(findings)}")
    print(f"High severity: {severity_counts['HIGH']}")
    print(f"Medium severity: {severity_counts['MEDIUM']}")
    print(f"Low severity: {severity_counts['LOW']}")
    print(f"Markdown report: {MARKDOWN_REPORT}")
    print(f"CSV report: {CSV_REPORT}")


if __name__ == "__main__":
    main()
