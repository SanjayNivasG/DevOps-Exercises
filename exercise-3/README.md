# ArgoCD OutOfSync Production Incident

## Project Overview

This project demonstrates how ArgoCD detects configuration drift between the Git repository and a Kubernetes cluster.

I deployed a Node.js application to Kubernetes using Docker and ArgoCD. Then I manually modified the deployment to simulate a real production incident and investigated how ArgoCD detected it.

---

# Technologies Used

* Git & GitHub
* Jenkins
* Docker
* Docker Hub
* Kubernetes (Minikube)
* ArgoCD
* Node.js
* Express.js

---

# Architecture

```text
Developer
    │
    ▼
GitHub
    │
    ▼
Jenkins
    │
    ▼
Docker Image
    │
    ▼
Docker Hub
    │
    ▼
Kubernetes
    │
    ▼
ArgoCD
```

---


# What I Implemented

* Built a Node.js application.
* Created a Docker image.
* Pushed the image to Docker Hub.
* Deployed the application to Kubernetes.
* Managed Kubernetes deployment using ArgoCD.
* Simulated a production configuration drift.

---

# Incident Scenario

### Desired State (Git)

```yaml
replicas: 3
```

### Manual Change

```bash
kubectl scale deployment student-app --replicas=5
```

### Result

* Git: **3 Replicas**
* Kubernetes: **5 Replicas**

ArgoCD detected the difference and reported:

* **Health:** Healthy
* **Sync Status:** OutOfSync

---

# Investigation

### What changed?

The Deployment replica count changed from **3** to **5**.

### Who changed it?

The deployment was manually updated using the `kubectl scale` command.

### Why was the application Healthy?

All application pods were running successfully, so the application was available.

### Why was it OutOfSync?

The live Kubernetes configuration no longer matched the desired configuration stored in Git.

---

# Solution

The deployment was synchronized with Git using ArgoCD, which restored the desired state.

To avoid similar issues:

* Use Git as the single source of truth.
* Avoid manual changes in production.
* Enable ArgoCD Auto Sync.
* Enable ArgoCD Self Heal.

---


# What I Learned

* GitOps workflow
* ArgoCD deployment management
* Kubernetes Deployments and Services
* Configuration drift detection
* Difference between **Healthy** and **OutOfSync**
* Production incident investigation

---

