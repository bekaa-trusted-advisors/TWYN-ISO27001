---
document_id: GUIDE-GAP-005
title: Implementation Guide - GAP-005: AWS Support Level Decision
version: 1.0
date: 2026-05-26
---

# GAP-005: AWS Support Level Decision

## Overview
Implementation guide for resolving GAP-005 (see GitHub Issue #5 for full context).

## Technical Guide

**Options**:\n- Developer: €29/month, email only, 12-24h response\n- Business: €100+/month, phone 24/7, <1h critical response\n**Decision Matrix**:\n- Biometric data criticality: HIGH → Business recommended\n- DevOps SPOF: HIGH → Business provides backup escalation\n- Cost: €1.5k/year acceptable for production\n**Action**: CEO approval, upgrade in AWS console\n**ETA**: 2 hours (analysis + approval)

## Prerequisites
- See GitHub Issue #5 for complete prerequisites
- Required permissions, tools, access documented there

## Success Criteria
- ✅ GAP closed
- ✅ Evidence collected for audit
- ✅ CAR completed (if applicable)
- ✅ Validation tests pass

## Troubleshooting
Common issues and solutions documented in GitHub Issue #5 comments.

## Related Documents
- GitHub Issue: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/5
- CAR Log: SGSI-CAR-001
- Risk Register: SGSI-RISK-002

## Owner
See GitHub Issue #5 for RACI details.
