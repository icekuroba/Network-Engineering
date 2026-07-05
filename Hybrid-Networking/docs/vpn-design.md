# VPN Design

## Objective

This document describes the site-to-site VPN design used to connect the on-premises enterprise network with the cloud network.

## VPN Model

The design assumes a site-to-site VPN tunnel between:

- On-premises edge router or firewall
- Cloud VPN gateway

## Traffic Selectors

Example traffic that should be allowed through the VPN:

| On-Premises Network | Cloud Network |
|---|---|
| 192.168.10.0/24 | 10.10.2.0/24 |
| 192.168.20.0/24 | 10.10.2.0/24 |
| 192.168.30.0/24 | 10.10.1.0/24 |
| 192.168.30.0/24 | 10.10.2.0/24 |
| 192.168.30.0/24 | 10.10.3.0/24 |

## Design Considerations

- Use non-overlapping address spaces.
- Restrict VPN traffic to required networks.
- Validate both forward and return routes.
- Apply firewall rules on both sides.
- Monitor tunnel status and dropped traffic.
