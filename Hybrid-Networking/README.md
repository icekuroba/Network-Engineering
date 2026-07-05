# Hybrid Networking

This project contains a hybrid network connectivity blueprint focused on connecting an on-premises enterprise network with a cloud network using site-to-site VPN concepts, routing design, segmentation, and security controls.

The goal is to document a practical hybrid networking architecture that can be used as a reference for enterprise network design, cloud connectivity, and troubleshooting.

## Project Goal

Design a secure and organized hybrid network architecture that connects:

- An on-premises enterprise network
- A cloud virtual network
- A site-to-site VPN connection
- Segmented user, server, management, and cloud subnets
- Security controls for controlled traffic flow

## Architecture Summary

```text
On-Premises Network
├── Users VLAN
├── Servers VLAN
├── Management VLAN
└── Edge Router / Firewall
        │
        │ Site-to-Site VPN
        │
Cloud Network
├── Public Subnet
├── Private Application Subnet
├── Database Subnet
└── Cloud Security Rules
```

## Repository Structure

```text
Hybrid-Networking/
├── README.md
├── diagrams/
│   └── hybrid-network-blueprint.mmd
├── docs/
│   ├── network-design.md
│   ├── ip-addressing-plan.md
│   ├── routing-plan.md
│   ├── security-controls.md
│   └── vpn-design.md
├── checklists/
│   ├── deployment-checklist.md
│   └── troubleshooting-checklist.md
├── reports/
│   └── design-summary.md
└── screenshots/
```

## Main Topics

- Hybrid network design
- Site-to-site VPN concepts
- IP addressing planning
- Cloud and on-premises routing
- Network segmentation
- Security rules and firewall controls
- Troubleshooting methodology
- Technical documentation

## Tools and Concepts

- Enterprise networking
- Cloud networking concepts
- VPN site-to-site design
- Routing tables
- Firewall rules
- Network segmentation
- Markdown documentation
- Mermaid diagrams

## Project Documents

| Document | Purpose |
|---|---|
| `docs/network-design.md` | Explains the hybrid architecture |
| `docs/ip-addressing-plan.md` | Defines the IP addressing scheme |
| `docs/routing-plan.md` | Documents routing between on-prem and cloud |
| `docs/security-controls.md` | Defines firewall and segmentation rules |
| `docs/vpn-design.md` | Explains the VPN design |
| `checklists/deployment-checklist.md` | Lists validation steps before deployment |
| `checklists/troubleshooting-checklist.md` | Provides troubleshooting steps |
| `reports/design-summary.md` | Summarizes the complete design |

## Security Note

This project is a design blueprint for educational and authorized lab environments only.