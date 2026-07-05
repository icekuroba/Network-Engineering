# IP Addressing Plan

## On-Premises Network

| Segment | Network | Purpose |
|---|---|---|
| Users VLAN | 192.168.10.0/24 | End-user devices |
| Servers VLAN | 192.168.20.0/24 | Internal servers |
| Management VLAN | 192.168.30.0/24 | Network management |
| VPN Transit | 172.16.0.0/30 | VPN tunnel addressing |

## Cloud Network

| Segment | Network | Purpose |
|---|---|---|
| Public Subnet | 10.10.1.0/24 | Public-facing services |
| Private App Subnet | 10.10.2.0/24 | Application servers |
| Database Subnet | 10.10.3.0/24 | Database workloads |

## Design Considerations

- Avoid overlapping IP ranges between on-premises and cloud.
- Reserve separate subnets for users, servers, management, applications, and databases.
- Keep database workloads in private subnets.
- Use clear IP documentation to simplify routing and troubleshooting.
