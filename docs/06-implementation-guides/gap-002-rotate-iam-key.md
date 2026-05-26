---
document_id: GUIDE-GAP-002
title: Implementation Guide - GAP-002: Rotate IAM Access Key (tmpsaasboost)
version: 1.0
date: 2026-05-26
---

# GAP-002: Rotate IAM Access Key (tmpsaasboost)

## Overview
Implementation guide for resolving GAP-002 (see GitHub Issue #2 for full context).

## Technical Guide

**Steps**:\n1. `aws iam list-access-keys --user tmpsaasboost`\n2. Generate new key: `aws iam create-access-key --user tmpsaasboost`\n3. Update apps/CI/CD with new key\n4. Test applications\n5. Deactivate old key: `aws iam update-access-key --access-key-id AKIAOLD --status Inactive`\n6. Wait 7 days, then delete: `aws iam delete-access-key --access-key-id AKIAOLD`\n**Automation**: AWS Secrets Manager auto-rotation\n**ETA**: 2 hours

## Prerequisites
- See GitHub Issue #2 for complete prerequisites
- Required permissions, tools, access documented there

## Success Criteria
- ✅ GAP closed
- ✅ Evidence collected for audit
- ✅ CAR completed (if applicable)
- ✅ Validation tests pass

## Troubleshooting
Common issues and solutions documented in GitHub Issue #2 comments.

## Related Documents
- GitHub Issue: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/2
- CAR Log: SGSI-CAR-001
- Risk Register: SGSI-RISK-002

## Owner
See GitHub Issue #2 for RACI details.
