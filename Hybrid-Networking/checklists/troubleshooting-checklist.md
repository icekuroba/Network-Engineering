# Hybrid Network Troubleshooting Checklist

## VPN Issues

- [ ] Is the VPN tunnel up?
- [ ] Are both VPN peers reachable?
- [ ] Are the correct traffic selectors configured?
- [ ] Are encryption settings compatible?

## Routing Issues

- [ ] Does on-premises have routes to cloud networks?
- [ ] Does cloud have routes to on-premises networks?
- [ ] Is return traffic routed correctly?
- [ ] Are there overlapping IP ranges?

## Firewall Issues

- [ ] Is traffic allowed on the on-premises firewall?
- [ ] Is traffic allowed by cloud security rules?
- [ ] Are management ports restricted?
- [ ] Are database ports protected?

## DNS Issues

- [ ] Can on-premises resolve cloud private names?
- [ ] Can cloud workloads resolve internal names?
- [ ] Are DNS forwarders configured if needed?

## Validation

- [ ] Test from users subnet to cloud app subnet.
- [ ] Test from servers subnet to cloud app subnet.
- [ ] Test from management subnet to cloud resources.
- [ ] Confirm database subnet is not publicly accessible.
