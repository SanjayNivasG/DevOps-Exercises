# Exercise 22: Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler on Amazon EKS

## Overview

This project demonstrates the implementation of **Horizontal Pod Autoscaler (HPA)** and **Cluster Autoscaler** on **Amazon Elastic Kubernetes Service (EKS)**. The application automatically scales pods based on CPU utilization and provisions additional worker nodes when existing nodes cannot schedule new workloads.

By combining HPA, Metrics Server, and Cluster Autoscaler, the Kubernetes platform automatically adjusts application capacity based on real-time demand.

---

# Objective

Build an auto-scaling Kubernetes platform on Amazon EKS by implementing:

- Horizontal Pod Autoscaler (HPA)
- Cluster Autoscaler
- Metrics Server
- IAM Roles for Service Accounts (IRSA)
- Amazon EC2 Auto Scaling Groups
- CPU-based autoscaling
- Load testing to validate scaling

---

# Architecture

```text
                  Load Generator
               (BusyBox / wget)
                       │
                       ▼
                NGINX Application
                       │
                       ▼
        Horizontal Pod Autoscaler
              Scale Pods (2 → 20)
                       │
                       ▼
          Cluster Autoscaler
              Scale Nodes (2 → 3)
                       │
                       ▼
     Amazon EKS Managed Node Group
```

---

# Technologies Used

- Amazon EKS
- Kubernetes
- AWS CLI
- eksctl
- kubectl
- Amazon EC2 Auto Scaling Groups
- Metrics Server
- Horizontal Pod Autoscaler
- Cluster Autoscaler
- IAM Roles for Service Accounts (IRSA)
- Helm
- NGINX
- BusyBox

---

# Features

- Deploy applications on Amazon EKS
- Configure Metrics Server
- Configure Horizontal Pod Autoscaler
- Configure Cluster Autoscaler
- IAM Roles for Service Accounts (IRSA)
- Auto-discovery of EC2 Auto Scaling Groups
- Automatic pod scaling
- Automatic worker node scaling
- CPU utilization monitoring
- Load testing using BusyBox
- Fully automated scaling

---

# Project Structure

```text
exercise-22/
│
├── deployment.yaml
├── service.yaml
├── hpa.yaml
├── cluster-autoscaler-policy.json
├── cluster-autoscaler-autodiscover.yaml
├── namespace.yaml
└── README.md
```

---

# Prerequisites

Before deploying the project, ensure the following are installed.

- AWS CLI
- kubectl
- eksctl
- Helm
- Amazon EKS Cluster
- IAM OIDC Provider
- Metrics Server
- AWS IAM permissions

Configure AWS credentials.

```bash
aws configure
```

---

# Implementation Steps

## Step 1 – Create Amazon EKS Cluster

Provision an Amazon EKS cluster using **eksctl**.

```bash
eksctl create cluster \
--name autoscaling-cluster \
--region us-east-1 \
--nodegroup-name workers \
--node-type t3.medium \
--nodes 2
```

---

## Step 2 – Verify Cluster

```bash
kubectl get nodes
```

---

## Step 3 – Install Metrics Server

Deploy Metrics Server to collect CPU and memory metrics.

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Verify installation.

```bash
kubectl get pods -n kube-system
```

---

## Step 4 – Deploy Application

Deploy the sample NGINX application.

```bash
kubectl apply -f deployment.yaml

kubectl apply -f service.yaml
```

---

## Step 5 – Configure Horizontal Pod Autoscaler

Deploy the HPA configuration.

```bash
kubectl apply -f hpa.yaml
```

Verify HPA.

```bash
kubectl get hpa
```

---

## Step 6 – Configure IAM Roles for Service Accounts (IRSA)

Grant Cluster Autoscaler secure permissions to access AWS APIs without using AWS access keys.

Configure:

- IAM Policy
- IAM Role
- Kubernetes Service Account
- OIDC Provider

---

## Step 7 – Install Cluster Autoscaler

Deploy Cluster Autoscaler.

```bash
kubectl apply -f cluster-autoscaler-autodiscover.yaml
```

Verify deployment.

```bash
kubectl get deployment -n kube-system
```

---

## Step 8 – Generate Load

Create a BusyBox pod to continuously send requests.

```bash
kubectl run load-generator \
--image=busybox \
--restart=Never \
-- /bin/sh
```

Inside the pod:

```bash
while true; do
wget -q -O- http://nginx-service;
done
```

---

## Step 9 – Verify Autoscaling

Monitor pod scaling.

```bash
kubectl get hpa -w
```

Monitor node scaling.

```bash
kubectl get nodes -w
```

---

# Verification Commands

## Worker Nodes

```bash
kubectl get nodes
```

---

## Deployments

```bash
kubectl get deployment
```

---

## Horizontal Pod Autoscaler

```bash
kubectl get hpa
```

---

## Pods

```bash
kubectl get pods
```

---

## Pod Metrics

```bash
kubectl top pods
```

---

## Node Metrics

```bash
kubectl top nodes
```

---

## Auto Scaling Groups

```bash
aws autoscaling describe-auto-scaling-groups \
--query "AutoScalingGroups[*].[AutoScalingGroupName,DesiredCapacity,MinSize,MaxSize]" \
--output table
```

---

## Cluster Autoscaler Logs

```bash
kubectl logs \
-n kube-system \
deployment/cluster-autoscaler \
--tail=20
```

---

# Expected Results

- Amazon EKS cluster deployed successfully.
- Metrics Server collecting CPU metrics.
- Horizontal Pod Autoscaler automatically scales application pods.
- Cluster Autoscaler provisions additional worker nodes.
- IRSA configured successfully.
- Auto Scaling Group discovered automatically.
- BusyBox load generator triggers autoscaling.
- Worker nodes scale based on application demand.

---

# Monitoring Flow

```text
BusyBox Load
      │
      ▼
NGINX Deployment
      │
      ▼
CPU Utilization
      │
      ▼
Metrics Server
      │
      ▼
Horizontal Pod Autoscaler
      │
      ▼
Additional Pods
      │
      ▼
Insufficient Resources
      │
      ▼
Cluster Autoscaler
      │
      ▼
New Worker Node
```

---

# Learning Outcomes

- Amazon EKS Cluster Management
- Kubernetes Resource Scaling
- Horizontal Pod Autoscaler (HPA)
- Cluster Autoscaler
- Metrics Server
- IAM Roles for Service Accounts (IRSA)
- Amazon EC2 Auto Scaling Groups
- Kubernetes Resource Monitoring
- Load Testing
- Production Autoscaling Architecture

---

# Cleanup

Delete Kubernetes resources.

```bash
kubectl delete -f hpa.yaml

kubectl delete -f deployment.yaml

kubectl delete -f service.yaml
```

Delete the Amazon EKS cluster.

```bash
eksctl delete cluster \
--name autoscaling-cluster \
--region us-east-1
```

---

# Author

**Sanjay Nivas G**

**DevOps Engineer | AWS | Kubernetes | Docker | Terraform | GitOps | ArgoCD**
