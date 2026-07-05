# Routing Plan

## Objective

This document defines the routing logic required for communication between the on-premises network and the cloud network.

## On-Premises Routes

The on-premises edge router or firewall should know how to reach the cloud networks.

Example cloud routes:

| Destination | Next Hop |
|---|---|
| 10.10.1.0/24 | VPN Tunnel |
| 10.10.2.0/24 | VPN Tunnel |
| 10.10.3.0/24 | VPN Tunnel |

## Cloud Routes

The cloud route table should know how to reach the on-premises networks.

Example on-premises routes:

| Destination | Next Hop |
|---|---|
| 192.168.10.0/24 | VPN Gateway |
| 192.168.20.0/24 | VPN Gateway |
| 192.168.30.0/24 | VPN Gateway |

## Troubleshooting Notes

If the VPN is up but traffic does not pass, check:

- Missing routes
- Incorrect next hop
- Overlapping networks
- Firewall rules
- Cloud security rules
- Return path routing
