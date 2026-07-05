import re
from collections import Counter
from pathlib import Path


def add_finding(findings, severity, file_name, rule, message, recommendation):
    findings.append({
        "severity": severity,
        "file": file_name,
        "rule": rule,
        "message": message,
        "recommendation": recommendation
    })


def read_config(path):
    return Path(path).read_text(encoding="utf-8")


def get_blocks(config_text, block_keyword):
    lines = config_text.splitlines()
    blocks = []
    current_block = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith(block_keyword):
            if current_block:
                blocks.append("\n".join(current_block))
            current_block = [stripped]
        elif current_block:
            if stripped == "!" or stripped == "end":
                blocks.append("\n".join(current_block))
                current_block = []
            else:
                current_block.append(stripped)

    if current_block:
        blocks.append("\n".join(current_block))

    return blocks


def audit_config(path):
    findings = []
    config_path = Path(path)
    file_name = config_path.name
    config = read_config(config_path)
    config_lower = config.lower()

    # Rule 1: service password-encryption missing
    if "service password-encryption" not in config_lower:
        add_finding(
            findings,
            "LOW",
            file_name,
            "service password-encryption missing",
            "The configuration does not enable service password-encryption.",
            "Enable service password-encryption to reduce exposure of plaintext passwords in the configuration."
        )

    # Rule 2: enable secret missing
    if not re.search(r"^enable secret", config_lower, re.MULTILINE):
        add_finding(
            findings,
            "HIGH",
            file_name,
            "enable secret missing",
            "The configuration does not use enable secret.",
            "Use enable secret instead of enable password for privileged EXEC access."
        )

    # Rule 3: enable password used
    if re.search(r"^enable password", config_lower, re.MULTILINE):
        add_finding(
            findings,
            "MEDIUM",
            file_name,
            "enable password used",
            "The configuration uses enable password, which is weaker than enable secret.",
            "Replace enable password with enable secret."
        )

    # Rule 4: plaintext passwords
    if re.search(r"password 0 |username .* password 0 ", config_lower):
        add_finding(
            findings,
            "MEDIUM",
            file_name,
            "plaintext password detected",
            "A plaintext password was detected in the configuration.",
            "Use stronger secret-based credentials and avoid storing plaintext passwords."
        )

    # Rule 5: Telnet enabled
    if "transport input telnet" in config_lower or "transport input all" in config_lower:
        add_finding(
            findings,
            "HIGH",
            file_name,
            "telnet enabled",
            "VTY lines allow Telnet access.",
            "Disable Telnet and allow SSH only with transport input ssh."
        )

    # Rule 6: VTY login local missing
    vty_blocks = get_blocks(config, "line vty")
    for block in vty_blocks:
        block_lower = block.lower()
        if "login local" not in block_lower:
            add_finding(
                findings,
                "MEDIUM",
                file_name,
                "vty login local missing",
                "VTY lines do not use login local.",
                "Configure local user authentication with login local on VTY lines."
            )

    # Rule 7: SNMP public/private community
    if re.search(r"snmp-server community (public|private)\b", config_lower):
        add_finding(
            findings,
            "HIGH",
            file_name,
            "weak snmp community",
            "SNMP uses a default or weak community string.",
            "Replace public/private SNMP communities with strong values or use SNMPv3."
        )

    # Rule 8: interfaces without description
    interface_blocks = get_blocks(config, "interface ")
    for block in interface_blocks:
        block_lower = block.lower()
        interface_name = block.splitlines()[0].replace("interface ", "")

        if "description" not in block_lower and "shutdown" not in block_lower:
            add_finding(
                findings,
                "LOW",
                file_name,
                "interface description missing",
                f"Interface {interface_name} is active or configured without a description.",
                "Add interface descriptions to improve documentation and troubleshooting."
            )

        if "description unused" in block_lower and "shutdown" not in block_lower:
            add_finding(
                findings,
                "MEDIUM",
                file_name,
                "unused interface not shutdown",
                f"Interface {interface_name} is marked as unused but is not shutdown.",
                "Shutdown unused interfaces to reduce unauthorized access risk."
            )

    # Rule 9: OSPF passive-interface default missing
    ospf_blocks = get_blocks(config, "router ospf")
    for block in ospf_blocks:
        if "passive-interface default" not in block.lower():
            add_finding(
                findings,
                "MEDIUM",
                file_name,
                "ospf passive-interface default missing",
                "OSPF is configured without passive-interface default.",
                "Use passive-interface default and explicitly enable OSPF only on required neighbor links."
            )

    return findings


def audit_multiple_configs(config_files):
    findings = []

    for config_file in config_files:
        findings.extend(audit_config(config_file))

    return findings


def count_by_severity(findings):
    counts = Counter(finding["severity"] for finding in findings)

    return {
        "HIGH": counts.get("HIGH", 0),
        "MEDIUM": counts.get("MEDIUM", 0),
        "LOW": counts.get("LOW", 0),
        "INFO": counts.get("INFO", 0),
    }
