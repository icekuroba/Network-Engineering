# Security Controls

## Objective

This document defines basic security controls for the hybrid network design.

## Recommended Controls

### Segmentation

Separate traffic by function:

- Users
- Servers
- Management
- Public cloud workloads
- Private cloud workloads
- Database workloads

### Access Control

Recommended traffic rules:

| Source | Destination | Allowed Traffic |
|---|---|---|
| Users VLAN | Private App Subnet | HTTPS |
| Servers VLAN | Private App Subnet | Required application ports |
| Management VLAN | Network devices | SSH / HTTPS |
| Private App Subnet | Database Subnet | Database port only |
| Internet | Database Subnet | Deny |
| Internet | Management VLAN | Deny |

### Management Access

Management access should be restricted to trusted administrative networks only.

### Database Protection

Database subnets should not be directly exposed to the internet.

## Defensive Value

These controls reduce unnecessary exposure and help protect hybrid environments from misconfiguration and lateral movement.
