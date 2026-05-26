---
document_id: GUIDE-GAP-001
title: Implementation Guide - GAP-001: Enable MFA on AWS Root Account
version: 1.0
date: 2026-05-26
---

# GAP-001: Enable MFA on AWS Root Account

## Overview
Implementation guide for resolving GAP-001 (see GitHub Issue #1 for full context).

## Technical Guide

**Prerequisites**: YubiKey (~€70), Physical safe\n**Steps**:\n1. Login AWS root (account 992382542028)\n2. IAM → Security Credentials → MFA\n3. Register hardware MFA device\n4. Test login with MFA\n5. Store YubiKey in CEO office safe\n6. Document location in Asset Inventory\n**Validation**: `aws iam get-account-summary | grep AccountMFAEnabled` = 1\n**ETA**: 1 hour

## Prerequisites
- See GitHub Issue #1 for complete prerequisites
- Required permissions, tools, access documented there

## Success Criteria
- ✅ GAP closed
- ✅ Evidence collected for audit
- ✅ CAR completed (if applicable)
- ✅ Validation tests pass

## Troubleshooting
Common issues and solutions documented in GitHub Issue #1 comments.

## Related Documents
- GitHub Issue: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/1
- CAR Log: SGSI-CAR-001
- Risk Register: SGSI-RISK-002

## Owner
See GitHub Issue #1 for RACI details.
