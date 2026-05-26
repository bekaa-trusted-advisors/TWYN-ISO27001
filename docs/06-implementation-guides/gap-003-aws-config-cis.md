---
document_id: GUIDE-GAP-003
title: Implementation Guide - GAP-003: Implement AWS Config + CIS Benchmarks
version: 1.0
date: 2026-05-26
---

# GAP-003: Implement AWS Config + CIS Benchmarks

## Overview
Implementation guide for resolving GAP-003 (see GitHub Issue #3 for full context).

## Technical Guide

**Phase 1 - Enable Config**:\n```bash\naws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=arn:aws:iam::...\naws configservice put-delivery-channel --delivery-channel name=default,s3BucketName=config-bucket\naws configservice start-configuration-recorder --configuration-recorder-name default\n```\n**Phase 2 - CIS Rules**:\nEnable AWS Config Managed Rules: access-keys-rotated, mfa-enabled-for-iam-console-access, etc.\n**Phase 3 - Security Hub**: Enable CIS AWS Foundations Benchmark standard\n**Cost**: ~€50-60/month\n**ETA**: 8-12 hours

## Prerequisites
- See GitHub Issue #3 for complete prerequisites
- Required permissions, tools, access documented there

## Success Criteria
- ✅ GAP closed
- ✅ Evidence collected for audit
- ✅ CAR completed (if applicable)
- ✅ Validation tests pass

## Troubleshooting
Common issues and solutions documented in GitHub Issue #3 comments.

## Related Documents
- GitHub Issue: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/3
- CAR Log: SGSI-CAR-001
- Risk Register: SGSI-RISK-002

## Owner
See GitHub Issue #3 for RACI details.
