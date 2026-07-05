# Network Design

## Objective

This document describes a hybrid network architecture that connects an on-premises enterprise network with a cloud virtual network using a site-to-site VPN model.

## Design Components

### On-Premises Network

The on-premises network is divided into three main segments:

- Users VLAN
- Servers VLAN
- Management VLAN

These segments connect through an edge router or firewall that controls traffic toward the cloud network.

### Cloud Network

The cloud network is divided into:

- Public subnet
- Private application subnet
- Database subnet

The public subnet may host externally reachable services. The private application and database subnets should not be directly exposed to the internet.

### Connectivity

Connectivity between the on-premises network and the cloud network is provided through a site-to-site VPN tunnel.

## Design Goal

The goal is to provide controlled connectivity between enterprise users, internal servers, and cloud workloads while maintaining segmentation and security boundaries.
