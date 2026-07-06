# Security

This document outlines the security policy for falcon-mcp-extended, an independent community project (not affiliated with CrowdStrike).

## Supported Versions

Security fixes are released for the most recent version only.

## Reporting a Potential Security Vulnerability

To report a suspected vulnerability in this project:

+ Use [GitHub private vulnerability reporting](https://github.com/rijul170/falcon-mcp/security/advisories/new) (preferred), or
+ Open an issue in this repository if the vulnerability is not sensitive.

Please do not report vulnerabilities in this project to CrowdStrike — they do not maintain it. Vulnerabilities in the CrowdStrike Falcon platform or the official falcon-mcp server should be reported to CrowdStrike via oss-security@crowdstrike.com.

## Disclosure and Mitigation Process

Upon receiving a security report, the issue will be triaged and, once confirmed, patched in the most recent version. Reporters will be credited in the release notes unless they prefer otherwise.

## Scope Notes

This server executes API calls against your CrowdStrike Falcon tenant with the credentials you provide. Review the [Security Considerations](../README.md#security-considerations) section of the README for hardening guidance (read-only mode, destructive tool gating, credential scoping, and network exposure).
