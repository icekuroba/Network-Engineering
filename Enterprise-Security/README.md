# Enterprise Security

This project contains a Python-based network device configuration auditor focused on enterprise security hardening.

The tool analyzes sample router and switch configuration files, detects insecure settings or weak practices, classifies findings by severity, and generates Markdown and CSV reports.

## Project Goal

The goal is to practice enterprise network security auditing by reviewing device configurations and identifying common hardening issues before they become operational or security risks.

## What the Auditor Detects

The current version detects:

- Telnet enabled on VTY lines
- Missing `enable secret`
- Use of weaker `enable password`
- Plaintext passwords
- Missing `service password-encryption`
- VTY lines without `login local`
- Weak SNMP community strings such as `public` or `private`
- Interfaces without descriptions
- Unused interfaces not shut down
- OSPF without `passive-interface default`

## Project Structure

```text
Enterprise-Security/
├── README.md
├── data/
│   ├── sample_router_config.txt
│   └── sample_switch_config.txt
├── src/
│   ├── auditor.py
│   ├── report.py
│   └── main.py
├── reports/
│   ├── hardening-audit-report.md
│   └── hardening-audit-findings.csv
├── docs/
│   └── hardening-rules.md
└── screenshots/
```

## Tools Used

- Python 3
- Sample router configuration files
- Sample switch configuration files
- Markdown reporting
- CSV reporting
- Git/GitHub

## How to Run

From the project root:

```bash
python3 src/main.py
```

Expected output:

```text
Enterprise Security Hardening Auditor completed.
Configuration files analyzed: 2
Findings detected: ...
Markdown report: reports/hardening-audit-report.md
CSV report: reports/hardening-audit-findings.csv
```

## Generated Reports

The tool generates two report files:

```text
reports/hardening-audit-report.md
reports/hardening-audit-findings.csv
```

The Markdown report is useful for documentation and review.  
The CSV report is useful for filtering, sorting, and importing findings into other tools.

## Sample Findings

Example findings detected by the auditor:

```text
HIGH - Telnet enabled
MEDIUM - Enable password used
MEDIUM - Plaintext password detected
HIGH - Weak SNMP community
MEDIUM - OSPF passive-interface default missing
LOW - Service password-encryption missing
```

## Defensive Value

This project demonstrates how configuration review can help improve enterprise network security.

Hardening network device configurations helps reduce risks related to insecure remote access, weak authentication, poor interface documentation, and unnecessary service exposure.

## Future Improvements

- Add support for more configuration patterns.
- Add CLI arguments for custom configuration files.
- Add JSON output.
- Add severity scoring.
- Add remediation checklist generation.
- Add compliance-style summary.
- Add support for additional vendor-like configuration formats.
- Add screenshots of report output.

## Security Note

This project uses sample configurations for educational and authorized lab environments only.

Do not audit, scan, or analyze systems without permission.
