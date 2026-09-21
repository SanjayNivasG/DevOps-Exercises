ALB Ingress Failure Investigation

## Project Overview

This project demonstrates the investigation and troubleshooting process for an AWS Application Load Balancer (ALB) Ingress issue in an Amazon EKS cluster. The objective was to understand how the AWS Load Balancer Controller provisions ALBs, how subnet discovery works, and how to diagnose Ingress-related deployment issues in a production-like environment.

During this exercise, the AWS Load Balancer Controller was installed using Helm with IAM Roles for Service Accounts (IRSA). An application was deployed, exposed through a Kubernetes Service, and published using an ALB Ingress. The investigation also included validating subnet tags, analyzing controller logs, testing subnet tag removal, and restoring the environment.

---

# Architecture

```
Client
   │
   ▼
AWS Application Load Balancer (ALB)
   │
AWS Load Balancer Controller
   │
Kubernetes Ingress
   │
ClusterIP Service
   │
Payment Application Pods
```

---

# Objectives

* Deploy an application on Amazon EKS.
* Install and configure AWS Load Balancer Controller.
* Configure IAM Roles for Service Accounts (IRSA).
* Create an ALB-backed Kubernetes Ingress.
* Investigate ALB provisioning using controller logs.
* Validate subnet discovery and tagging.
* Simulate subnet tag changes.
* Restore the production environment after testing.

---

# Technologies Used

* Amazon EKS
* Kubernetes
* AWS Load Balancer Controller
* Application Load Balancer (ALB)
* IAM Roles for Service Accounts (IRSA)
* Helm
* AWS IAM
* AWS VPC
* AWS CLI
* kubectl

---

# Project Structure

```
Exercise-07-ALB-Ingress-Failure/
│
├── deployment.yaml
├── service.yaml
├── ingress.yaml
├── iam_policy.json
├── README.md
└── screenshots/
```

---

# Implementation Steps

## Step 1

Created a Kubernetes namespace for the application.

## Step 2

Deployed the Payment application with multiple replicas.

## Step 3

Created a ClusterIP Service for internal communication.

## Step 4

Configured an ALB Ingress resource.

## Step 5

Verified the Ingress resource and backend Service.

## Step 6

Configured OIDC provider for the EKS cluster.

## Step 7

Created an IAM policy required by the AWS Load Balancer Controller.

## Step 8

Configured IRSA using an IAM Service Account.

## Step 9

Installed the AWS Load Balancer Controller using Helm.

## Step 10

Verified controller deployment and controller logs.

## Step 11

Validated subnet tags used for ALB discovery.

## Step 12

Removed public subnet ALB tags to observe controller behavior.

## Step 13

Recreated the Ingress and monitored reconciliation.

## Step 14

Restored subnet tags to return the environment to a healthy state.

---

# Investigation Summary

The expected production incident described an ALB provisioning failure caused by subnet discovery issues.

The following investigation steps were completed:

* Verified Kubernetes Deployments
* Verified Services
* Verified Ingress configuration
* Installed AWS Load Balancer Controller
* Examined controller logs
* Verified IAM Role and Service Account
* Inspected public subnet tags
* Removed ALB subnet tags
* Recreated the Ingress resource
* Monitored controller reconciliation
* Restored subnet tags

---

# Findings

The AWS Load Balancer Controller successfully created the Application Load Balancer after installation.

Although the public subnet tags were temporarily removed, the controller continued to reconcile the Ingress successfully in this environment.

This behavior differs from older troubleshooting scenarios where removing `kubernetes.io/role/elb` resulted in an **"Unable to discover subnets"** error. The observed behavior is consistent with the controller version and EKS configuration used in this project.

---

# Skills Demonstrated

* Amazon EKS Administration
* Kubernetes Networking
* AWS Load Balancer Controller
* ALB Ingress Configuration
* IAM Roles for Service Accounts (IRSA)
* Helm Package Management
* AWS IAM Policy Management
* Kubernetes Troubleshooting
* Production Incident Investigation
* Controller Log Analysis
* AWS CLI
* kubectl

---

# Key Commands

```bash
kubectl get pods -A

kubectl get ingress -n payment

kubectl describe ingress payment-ingress -n payment

kubectl logs deployment/aws-load-balancer-controller -n kube-system

kubectl get deployment -n kube-system

helm list -n kube-system

aws ec2 describe-subnets

aws ec2 create-tags

aws ec2 delete-tags
```

---

# Learning Outcomes

* Understood the complete ALB Ingress workflow in Amazon EKS.
* Learned how the AWS Load Balancer Controller provisions ALBs.
* Configured secure AWS access using IRSA.
* Investigated Ingress reconciliation using controller logs.
* Explored subnet tagging and ALB discovery.
* Performed production-style troubleshooting and environment recovery.

---

# Conclusion

This exercise demonstrates a complete implementation and investigation of AWS ALB Ingress on Amazon EKS. It covers controller installation, IAM integration, Kubernetes networking, subnet validation, log analysis, and production-style troubleshooting. The project provides practical experience with diagnosing and validating ALB Ingress behavior in a real EKS environment.
