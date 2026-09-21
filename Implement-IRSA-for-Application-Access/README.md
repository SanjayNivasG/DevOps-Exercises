Implement IRSA for Application Access

## Project Overview

This project demonstrates how to securely access Amazon DynamoDB from an Amazon EKS application using **IAM Roles for Service Accounts (IRSA)** without storing AWS Access Keys inside Kubernetes.

IRSA allows Kubernetes Pods to assume an IAM Role using a Service Account, providing temporary AWS credentials and following AWS security best practices.

---

# Objective

Implement IAM Roles for Service Accounts (IRSA) so that an application running inside Amazon EKS can access DynamoDB without using AWS Access Keys.

---

# Architecture

```
Amazon EKS Cluster
        │
        ▼
Kubernetes Service Account
        │
        ▼
IAM Role (IRSA)
        │
        ▼
IAM Policy
        │
        ▼
Amazon DynamoDB
```

---

# Technologies Used

* Amazon EKS
* Kubernetes
* IAM Roles for Service Accounts (IRSA)
* AWS IAM
* OpenID Connect (OIDC)
* Amazon DynamoDB
* AWS CLI
* eksctl
* kubectl

---

# Project Structure

```
Exercise-17-IRSA/
│
├── manifests/
│   └── pod.yaml
│
├── screenshots/
│
├── dynamodb-policy.json
│
└── README.md
```

---

# Prerequisites

* AWS Account
* Amazon EKS Cluster
* kubectl
* eksctl
* AWS CLI
* IAM Permissions

---

# Implementation Steps

## Step 1 – Create Amazon EKS Cluster

Created an Amazon EKS cluster with managed worker nodes.

Verified cluster:

```bash
kubectl get nodes
```

---

## Step 2 – Enable OIDC Provider

Associated an OpenID Connect (OIDC) provider with the EKS cluster.

```bash
eksctl utils associate-iam-oidc-provider \
--cluster exercise17-irsa \
--region ap-south-1 \
--approve
```

---

## Step 3 – Create DynamoDB Table

Created a DynamoDB table named **Users**.

Partition Key

```
UserId (String)
```

---

## Step 4 – Create IAM Policy

Created a custom IAM policy allowing only:

* dynamodb:GetItem
* dynamodb:PutItem
* dynamodb:UpdateItem

This follows the Principle of Least Privilege.

---

## Step 5 – Create IAM Role and Service Account

Created an IAM Role and attached it to a Kubernetes Service Account using IRSA.

Service Account

```
dynamodb-sa
```

---

## Step 6 – Deploy Test Pod

Created an AWS CLI Pod using the Service Account.

```yaml
serviceAccountName: dynamodb-sa
```

---

## Step 7 – Verify IRSA

Verified that the Pod assumed the IAM Role instead of using AWS Access Keys.

Command

```bash
aws sts get-caller-identity
```

Result

```
AssumedRole
```

This confirms that IRSA is working successfully.

---

## Step 8 – Test DynamoDB Access

Successfully executed the following operations:

### PutItem

Inserted a new record into the DynamoDB table.

### GetItem

Retrieved the inserted record successfully.

### UpdateItem

Updated the existing record successfully.

---

# Verification

The following operations were successfully verified.

| Requirement                        | Status |
| ---------------------------------- | ------ |
| IAM Policy Created                 | ✅      |
| IAM Role Created                   | ✅      |
| OIDC Provider Configured           | ✅      |
| Kubernetes Service Account Created | ✅      |
| IRSA Working Successfully          | ✅      |
| DynamoDB PutItem                   | ✅      |
| DynamoDB GetItem                   | ✅      |
| DynamoDB UpdateItem                | ✅      |
| AWS Access Keys Used               | ❌ No   |

---

# Security Benefits

* No AWS Access Keys stored inside Kubernetes.
* Temporary AWS credentials are issued automatically.
* Fine-grained IAM permissions.
* Follows AWS security best practices.
* Reduces the risk of credential leakage.

---

# Learning Outcomes

Through this exercise, I learned:

* Amazon EKS authentication with IAM
* IAM Roles for Service Accounts (IRSA)
* OpenID Connect (OIDC)
* IAM Policies and Roles
* Kubernetes Service Accounts
* Secure access to AWS services from Kubernetes
* Amazon DynamoDB operations
* AWS security best practices

---

# Screenshots

* EKS Cluster Nodes
* OIDC Provider
* IAM Service Account
* DynamoDB Table
* Running Pod
* IRSA Assumed Role
* DynamoDB Operations

---

# Conclusion

This project successfully demonstrates secure access from an Amazon EKS application to Amazon DynamoDB using IAM Roles for Service Accounts (IRSA). The application performed DynamoDB operations without storing AWS Access Keys, following AWS security best practices and demonstrating a production-ready authentication approach.
