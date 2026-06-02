#!/usr/bin/env python3
"""
Linear Migration Script - TWYN ISO 27001 Project
Migrates 15 GitHub issues to Linear with full metadata

Requirements:
    pip install requests python-dotenv

Setup:
    1. Get Linear API key: https://linear.app/bekaa/settings/api
    2. Get Team ID: https://linear.app/bekaa/settings/teams
    3. Create .env file:
        LINEAR_API_KEY=lin_api_xxxxx
        LINEAR_TEAM_ID=bekaa-team-id
        LINEAR_PROJECT_ID=aegis-compliance-project-id

Usage:
    python linear-migration.py
"""

import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LINEAR_API_KEY = os.getenv('LINEAR_API_KEY')
LINEAR_TEAM_ID = os.getenv('LINEAR_TEAM_ID')
LINEAR_PROJECT_ID = os.getenv('LINEAR_PROJECT_ID', '')  # Optional

GRAPHQL_ENDPOINT = 'https://api.linear.app/graphql'

# GitHub Issues Data
ISSUES = [
    {
        'title': 'GAP-001: Enable MFA on AWS root account',
        'description': '''**Root Cause**: AWS root account (992382542028) does not have MFA enabled - CRITICAL security risk.

**Impact**:
- RISK-003 (score 20) - Unauthorized root access
- AWS FTR blocker (security requirement)
- ISO 27001 Annex A.5.17 (Authentication information) non-conformity

**Implementation**:
1. Login AWS root account (992382542028)
2. Navigate: IAM → Security Credentials → MFA
3. Register hardware MFA device (Yubikey or AWS Virtual MFA)
4. Test MFA login
5. Document MFA serial number in SGSI-ASSETS-001

**Validation**:
```bash
aws iam get-account-summary | grep AccountMFAEnabled
# Expected: 1
```

**Evidence**: Screenshot of MFA enabled + AWS Config rule compliance

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/1

**Related Docs**:
- docs/06-implementation-guides/gap-001-enable-mfa-root.md
- SGSI-POLICY-002 (Access Control Policy)
- SGSI-CAR-001 (CAR-001)''',
        'priority': 1,  # 1=Urgent, 2=High, 3=Medium, 4=Low
        'labels': ['critical', 'gap', 'car-001', 'devops', 'ftr-blocker'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-01',
        'estimate': 1,
    },
    {
        'title': 'GAP-002: Rotate IAM access key older than 90 days',
        'description': '''**Root Cause**: IAM user "tmpsaasboost" has access key last rotated >90 days ago (violates AWS FTR requirement).

**Impact**:
- RISK-006 (score 16) - Long-lived credentials exposure
- AWS FTR blocker (CIS AWS 1.4)
- ISO 27001 Annex A.5.18 (Access rights) non-conformity

**Implementation**:
1. Identify key: `aws iam list-access-keys --user-name tmpsaasboost`
2. Create new key: `aws iam create-access-key --user-name tmpsaasboost`
3. Update secrets in Secrets Manager (if automated deployments use this key)
4. Test new key functionality
5. Deactivate old key: `aws iam update-access-key --access-key-id OLD_KEY --status Inactive --user-name tmpsaasboost`
6. Wait 7 days → delete old key permanently

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/2

**Related Docs**:
- docs/06-implementation-guides/gap-002-rotate-iam-key.md
- SGSI-CAR-001 (CAR-002)
- SOP-004 (Secrets Management)''',
        'priority': 2,  # High
        'labels': ['high', 'gap', 'car-002', 'devops', 'ftr-blocker'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-08',
        'estimate': 2,
    },
    {
        'title': 'GAP-003: Implement AWS Config + CIS AWS Foundations Benchmark',
        'description': '''**Root Cause**: AWS Config not enabled → no automated compliance monitoring for CIS Benchmarks (AWS FTR blocker).

**Implementation**: See docs/06-implementation-guides/gap-003-aws-config-cis.md

**Cost**: ~€50/month (AWS Config recording + rules)

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/3''',
        'priority': 1,  # Urgent
        'labels': ['critical', 'gap', 'car-003', 'devops', 'ftr-blocker', 'infrastructure'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-08',
        'estimate': 8,
    },
    {
        'title': 'GAP-004: Test backup restoration (DR testing)',
        'description': '''**Root Cause**: Backups exist but restoration NEVER tested.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/4''',
        'priority': 2,  # High
        'labels': ['high', 'gap', 'car-004', 'devops', 'ftr-blocker', 'infrastructure'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-05',
        'estimate': 6,
    },
    {
        'title': 'GAP-005: AWS Support plan decision',
        'description': '''**Decision**: Upgrade to Business Support ($100/month) or document justification.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/5''',
        'priority': 2,  # High
        'labels': ['high', 'gap', 'ftr-blocker', 'management'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-05',
        'estimate': 1,
    },
    {
        'title': 'GAP-006: CEO signature on Information Security Policy',
        'description': '''**BLOCKER**: IS Policy not signed by CEO = MAJOR audit finding.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/6''',
        'priority': 1,  # Urgent
        'labels': ['critical', 'blocker', 'management', 'iso-27001'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-02',
        'estimate': 1,
    },
    {
        'title': 'GAP-007: ISO 27001 certification for Gestor SGSI (Ricardo)',
        'description': '''**Training**: ISO 27001 Lead Implementer (5 days, €2,400)

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/7''',
        'priority': 3,  # Medium
        'labels': ['medium', 'gap', 'training', 'iso-27001'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-07-01',
        'estimate': 40,
    },
    {
        'title': 'GAP-008: Hire Junior DevOps / SRE',
        'description': '''**SPOF Mitigation**: Hire second DevOps to reduce single point of failure.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/8''',
        'priority': 3,  # Medium
        'labels': ['medium', 'gap', 'people', 'management'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-08-31',
        'estimate': 80,
    },
    {
        'title': 'SOP-001: Onboarding and Offboarding Procedure',
        'description': '''**SOP**: Secure onboarding/offboarding process.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/9''',
        'priority': 3,  # Medium
        'labels': ['medium', 'sop', 'procedure', 'policy'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-15',
        'estimate': 8,
    },
    {
        'title': 'SOP-002: Change Management Procedure',
        'description': '''**SOP**: Control production changes to prevent incidents.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/10''',
        'priority': 3,  # Medium
        'labels': ['medium', 'sop', 'procedure', 'devops'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-20',
        'estimate': 6,
    },
    {
        'title': 'SOP-003: Remote Work Security Procedure',
        'description': '''**SOP**: Secure remote work practices.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/11''',
        'priority': 3,  # Medium
        'labels': ['medium', 'sop', 'procedure', 'policy'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-25',
        'estimate': 4,
    },
    {
        'title': 'SOP-004: Secrets Management Procedure',
        'description': '''**SOP**: Securely store, rotate, and access secrets.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/12''',
        'priority': 3,  # Medium
        'labels': ['medium', 'sop', 'procedure', 'devops'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-30',
        'estimate': 5,
    },
    {
        'title': 'SOP-005: IAM Access Recertification Procedure',
        'description': '''**SOP**: Quarterly IAM access review (least privilege).

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/13''',
        'priority': 3,  # Medium
        'labels': ['medium', 'sop', 'procedure', 'devops'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-07-05',
        'estimate': 6,
    },
    {
        'title': 'CERT-001: Contract ISO 27001 certification auditor',
        'description': '''**Milestone**: Hire accredited auditor for Stage 1+2 audits.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/14''',
        'priority': 2,  # High
        'labels': ['high', 'milestone', 'management', 'iso-27001'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-06-30',
        'estimate': 8,
    },
    {
        'title': 'TRAIN-001: Deploy Security Awareness Training platform',
        'description': '''**Milestone**: Implement KnowBe4 training + phishing simulations.

**GitHub Issue**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/15''',
        'priority': 3,  # Medium
        'labels': ['medium', 'milestone', 'training', 'iso-27001'],
        'assignee_email': 'resper@bekaa.eu',
        'due_date': '2026-07-31',
        'estimate': 20,
    },
]


def execute_graphql(query, variables=None):
    """Execute GraphQL query against Linear API"""
    headers = {
        'Authorization': LINEAR_API_KEY,
        'Content-Type': 'application/json'
    }

    payload = {'query': query}
    if variables:
        payload['variables'] = variables

    response = requests.post(GRAPHQL_ENDPOINT, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return None

    data = response.json()

    if 'errors' in data:
        print(f"❌ GraphQL Errors: {json.dumps(data['errors'], indent=2)}")
        return None

    return data.get('data')


def get_team_info():
    """Get team information"""
    query = """
    query {
      teams {
        nodes {
          id
          name
          key
        }
      }
    }
    """

    result = execute_graphql(query)
    if result and 'teams' in result:
        return result['teams']['nodes']
    return []


def get_or_create_labels(label_names):
    """Get or create labels and return their IDs"""
    label_ids = []

    # First, fetch existing labels
    query = """
    query($teamId: String!) {
      team(id: $teamId) {
        labels {
          nodes {
            id
            name
          }
        }
      }
    }
    """

    result = execute_graphql(query, {'teamId': LINEAR_TEAM_ID})

    existing_labels = {}
    if result and 'team' in result and result['team']:
        for label in result['team']['labels']['nodes']:
            existing_labels[label['name'].lower()] = label['id']

    # Get or create each label
    for label_name in label_names:
        label_lower = label_name.lower()
        if label_lower in existing_labels:
            label_ids.append(existing_labels[label_lower])
        else:
            # Create new label
            create_query = """
            mutation($teamId: String!, $name: String!) {
              issueLabelCreate(input: {
                teamId: $teamId
                name: $name
              }) {
                issueLabel {
                  id
                  name
                }
              }
            }
            """

            create_result = execute_graphql(create_query, {
                'teamId': LINEAR_TEAM_ID,
                'name': label_name
            })

            if create_result and 'issueLabelCreate' in create_result:
                new_label_id = create_result['issueLabelCreate']['issueLabel']['id']
                label_ids.append(new_label_id)
                print(f"  → Created label: {label_name}")

    return label_ids


def get_user_id(email):
    """Get Linear user ID from email"""
    query = """
    query {
      users {
        nodes {
          id
          email
          name
        }
      }
    }
    """

    result = execute_graphql(query)

    if result and 'users' in result:
        for user in result['users']['nodes']:
            if user['email'] == email:
                return user['id']

    return None


def create_issue(issue_data):
    """Create a single issue in Linear"""

    # Get label IDs
    label_ids = get_or_create_labels(issue_data['labels'])

    # Get assignee ID
    assignee_id = get_user_id(issue_data['assignee_email'])

    # Prepare mutation
    mutation = """
    mutation($teamId: String!, $title: String!, $description: String!, $priority: Int!, $labelIds: [String!], $assigneeId: String, $dueDate: TimelessDate, $estimate: Float, $projectId: String) {
      issueCreate(input: {
        teamId: $teamId
        title: $title
        description: $description
        priority: $priority
        labelIds: $labelIds
        assigneeId: $assigneeId
        dueDate: $dueDate
        estimate: $estimate
        projectId: $projectId
      }) {
        success
        issue {
          id
          identifier
          title
          url
        }
      }
    }
    """

    variables = {
        'teamId': LINEAR_TEAM_ID,
        'title': issue_data['title'],
        'description': issue_data['description'],
        'priority': issue_data['priority'],
        'labelIds': label_ids,
        'assigneeId': assignee_id,
        'dueDate': issue_data['due_date'],
        'estimate': issue_data['estimate'],
    }

    if LINEAR_PROJECT_ID:
        variables['projectId'] = LINEAR_PROJECT_ID

    result = execute_graphql(mutation, variables)

    if result and 'issueCreate' in result:
        if result['issueCreate']['success']:
            issue = result['issueCreate']['issue']
            print(f"✅ Created: {issue['title'][:50]}... ({issue['identifier']}) - {issue['url']}")
            return issue
        else:
            print(f"❌ Failed to create: {issue_data['title']}")

    return None


def main():
    print("🚀 Linear Migration Script - TWYN ISO 27001\n")

    # Validate environment
    if not LINEAR_API_KEY:
        print("❌ ERROR: LINEAR_API_KEY not found in .env file")
        print("\nSetup:")
        print("1. Get API key: https://linear.app/bekaa/settings/api")
        print("2. Create .env file with: LINEAR_API_KEY=lin_api_xxxxx")
        return

    if not LINEAR_TEAM_ID:
        print("❌ ERROR: LINEAR_TEAM_ID not found in .env file")
        print("\nFetching available teams...\n")
        teams = get_team_info()
        if teams:
            print("Available teams:")
            for team in teams:
                print(f"  - {team['name']} (ID: {team['id']}, Key: {team['key']})")
            print("\nAdd to .env: LINEAR_TEAM_ID=<team-id>")
        return

    print(f"📋 Team ID: {LINEAR_TEAM_ID}")
    if LINEAR_PROJECT_ID:
        print(f"📁 Project ID: {LINEAR_PROJECT_ID}")
    print(f"📊 Issues to migrate: {len(ISSUES)}\n")

    # Confirm
    confirm = input("Proceed with migration? (yes/no): ")
    if confirm.lower() != 'yes':
        print("❌ Migration cancelled")
        return

    print("\n🔄 Starting migration...\n")

    # Migrate each issue
    created_count = 0
    for i, issue_data in enumerate(ISSUES, 1):
        print(f"[{i}/{len(ISSUES)}] Creating: {issue_data['title'][:60]}...")
        issue = create_issue(issue_data)
        if issue:
            created_count += 1
        print()

    # Summary
    print("\n" + "="*60)
    print(f"✅ Migration complete: {created_count}/{len(ISSUES)} issues created")
    print("="*60)

    if LINEAR_PROJECT_ID:
        print(f"\n🔗 View project: https://linear.app/bekaa/project/{LINEAR_PROJECT_ID}")
    else:
        print(f"\n🔗 View issues: https://linear.app/bekaa/team")


if __name__ == '__main__':
    main()
