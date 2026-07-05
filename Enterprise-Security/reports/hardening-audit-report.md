# Enterprise Security Hardening Audit Report

## Summary

- Total findings: 11
- High severity: 4
- Medium severity: 5
- Low severity: 2

## Findings

### Finding 1: service password-encryption missing

- Severity: LOW
- File: sample_router_config.txt
- Message: The configuration does not enable service password-encryption.
- Recommendation: Enable service password-encryption to reduce exposure of plaintext passwords in the configuration.

### Finding 2: enable secret missing

- Severity: HIGH
- File: sample_router_config.txt
- Message: The configuration does not use enable secret.
- Recommendation: Use enable secret instead of enable password for privileged EXEC access.

### Finding 3: enable password used

- Severity: MEDIUM
- File: sample_router_config.txt
- Message: The configuration uses enable password, which is weaker than enable secret.
- Recommendation: Replace enable password with enable secret.

### Finding 4: plaintext password detected

- Severity: MEDIUM
- File: sample_router_config.txt
- Message: A plaintext password was detected in the configuration.
- Recommendation: Use stronger secret-based credentials and avoid storing plaintext passwords.

### Finding 5: telnet enabled

- Severity: HIGH
- File: sample_router_config.txt
- Message: VTY lines allow Telnet access.
- Recommendation: Disable Telnet and allow SSH only with transport input ssh.

### Finding 6: vty login local missing

- Severity: MEDIUM
- File: sample_router_config.txt
- Message: VTY lines do not use login local.
- Recommendation: Configure local user authentication with login local on VTY lines.

### Finding 7: weak snmp community

- Severity: HIGH
- File: sample_router_config.txt
- Message: SNMP uses a default or weak community string.
- Recommendation: Replace public/private SNMP communities with strong values or use SNMPv3.

### Finding 8: ospf passive-interface default missing

- Severity: MEDIUM
- File: sample_router_config.txt
- Message: OSPF is configured without passive-interface default.
- Recommendation: Use passive-interface default and explicitly enable OSPF only on required neighbor links.

### Finding 9: service password-encryption missing

- Severity: LOW
- File: sample_switch_config.txt
- Message: The configuration does not enable service password-encryption.
- Recommendation: Enable service password-encryption to reduce exposure of plaintext passwords in the configuration.

### Finding 10: telnet enabled

- Severity: HIGH
- File: sample_switch_config.txt
- Message: VTY lines allow Telnet access.
- Recommendation: Disable Telnet and allow SSH only with transport input ssh.

### Finding 11: vty login local missing

- Severity: MEDIUM
- File: sample_switch_config.txt
- Message: VTY lines do not use login local.
- Recommendation: Configure local user authentication with login local on VTY lines.

## Defensive Value

This audit helps identify insecure or weak network device configuration practices before they become operational or security risks.

## Security Note

This project uses sample configurations for educational and authorized lab environments only.