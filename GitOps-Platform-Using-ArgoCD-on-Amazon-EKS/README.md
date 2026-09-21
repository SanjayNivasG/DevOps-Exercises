# GitOps Platform Using ArgoCD on Amazon EKS

## Overview

This project demonstrates a **GitOps-based Continuous Deployment (CD) platform** using **ArgoCD** and **Amazon Elastic Kubernetes Service (EKS)**. The deployment process is fully automated, where ArgoCD continuously monitors a GitHub repository and synchronizes any changes to the Kubernetes cluster.

By adopting the GitOps approach, Git becomes the **single source of truth** for application deployment, ensuring consistency, automation, and easy rollback.

---

# Objective

Build a production-ready GitOps platform that provides:

- Amazon EKS Cluster
- ArgoCD Installation
- GitHub Integration
- Automatic Application Synchronization
- Self-Healing Kubernetes Resources
- Automatic Resource Pruning
- Multi-Environment Deployment (Dev, QA, Production)

---

# Architecture

```text
                Developer
                    │
          Git Commit & Push
                    │
                    ▼
            GitHub Repository
                    │
                    ▼
                ArgoCD Server
                    │
      Watches Repository Changes
                    │
                    ▼
            Amazon EKS Cluster
                    │
                    ▼
          Kubernetes Application
```

---

# Repository Structure

```text
gitops-platform/
│
├── gitops
│   ├── dev
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   │
│   ├── qa
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   │
│   └── prod
│       ├── deployment.yaml
│       └── service.yaml
│
├── argocd-app.yaml
└── README.md
```

---

# Technologies Used

- Amazon EKS
- Kubernetes
- ArgoCD
- GitHub
- Docker
- NGINX
- AWS EC2
- eksctl
- kubectl

---

# Features

## Auto Sync

ArgoCD continuously monitors the GitHub repository.

Whenever changes are committed, ArgoCD automatically synchronizes the Kubernetes cluster with the latest manifests.

---

## Self Heal

If a Kubernetes resource is modified or deleted manually, ArgoCD detects the configuration drift and automatically restores the resource to its desired state.

---

## Automatic Pruning

When Kubernetes manifests are removed from Git, ArgoCD automatically deletes the corresponding resources from the cluster.

---

# Prerequisites

Install the following tools before starting.

- AWS CLI
- kubectl
- eksctl
- Docker
- Git
- ArgoCD CLI (Optional)

Configure AWS credentials.

```bash
aws configure
```

---

# Deployment Steps

## Step 1: Create Amazon EKS Cluster

```bash
eksctl create cluster \
--name gitops-cluster \
--region us-east-1 \
--nodegroup-name workers \
--node-type t3.small \
--nodes 2
```

---

## Step 2: Verify Cluster

```bash
kubectl get nodes
```

---

## Step 3: Install ArgoCD

```bash
kubectl create namespace argocd

kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

---

## Step 4: Verify Installation

```bash
kubectl get pods -n argocd
```

---

## Step 5: Expose ArgoCD Server

```bash
kubectl patch svc argocd-server \
-n argocd \
-p '{"spec":{"type":"LoadBalancer"}}'
```

---

## Step 6: Get ArgoCD URL

```bash
kubectl get svc -n argocd
```

---

## Step 7: Retrieve Initial Admin Password

```bash
kubectl -n argocd \
get secret argocd-initial-admin-secret \
-o jsonpath="{.data.password}" | base64 -d
```

---

## Step 8: Create ArgoCD Application

```bash
kubectl apply -f argocd-app.yaml
```

---

# ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application

metadata:
  name: dev-app
  namespace: argocd

spec:
  project: default

  source:
    repoURL: https://github.com/<your-username>/<repository-name>.git
    targetRevision: HEAD
    path: gitops/dev

  destination:
    server: https://kubernetes.default.svc
    namespace: default

  syncPolicy:
    automated:
      prune: true
      selfHeal: true

    syncOptions:
      - CreateNamespace=true
```

---

# Demonstration

## Auto Sync

1. Update **deployment.yaml**.
2. Change replicas from **1** to **2**.
3. Commit the changes.
4. Push to GitHub.
5. ArgoCD automatically detects the commit.
6. The EKS cluster updates without manual deployment.

---

## Self Heal

Delete a running pod.

```bash
kubectl delete pod <pod-name>
```

ArgoCD immediately detects the missing resource.

A new pod is automatically created.

---

## Automatic Pruning

Delete **service.yaml** from the repository.

```bash
git add .

git commit -m "Remove service"

git push
```

ArgoCD synchronizes the repository.

The Kubernetes Service is automatically deleted.

---

# Validation

Check ArgoCD Applications

```bash
kubectl get applications -n argocd
```

Check Pods

```bash
kubectl get pods
```

Check Services

```bash
kubectl get svc
```

Check Deployments

```bash
kubectl get deployments
```

---

# Expected Results

- Amazon EKS cluster created successfully.
- ArgoCD installed and running.
- GitHub repository connected.
- Application deployed automatically.
- Auto Sync enabled.
- Self Heal functioning correctly.
- Pruning removes obsolete resources.
- Git remains the single source of truth.

---

# Learning Outcomes

- Understood GitOps workflow.
- Deployed Kubernetes applications using ArgoCD.
- Connected GitHub with Amazon EKS.
- Implemented Continuous Deployment.
- Configured Auto Sync.
- Implemented Self Heal.
- Configured Automatic Pruning.
- Managed Kubernetes deployments using Git.

---

# Project Workflow

```text
Developer
     │
Git Commit
     │
     ▼
GitHub Repository
     │
     ▼
ArgoCD
     │
Repository Monitoring
     │
     ▼
Amazon EKS
     │
     ▼
Kubernetes Deployment
```

---

# Cleanup

Delete the ArgoCD application.

```bash
kubectl delete application dev-app -n argocd
```

Delete the EKS cluster.

```bash
eksctl delete cluster --name gitops-cluster --region us-east-1
```

---

# Demo Video

Watch the complete project demonstration:

https://drive.google.com/file/d/1LiX4GY1wpUylbDQQWbDXcTSTmdH3ZSMt/view?usp=sharing

---

# Author

**Sanjay Nivas G**

**DevOps Engineer | AWS | Kubernetes | Docker | Terraform | GitOps | ArgoCD**
