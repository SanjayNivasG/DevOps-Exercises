# Exercise 23 - Simple CI/CD Pipeline (GitHub → Docker → ArgoCD Concept)

## Project Overview

This project demonstrates a simple CI/CD pipeline using GitHub, Docker, GitHub Actions, Kubernetes manifests, and the ArgoCD deployment concept.

The application is a simple Python Flask web application that is containerized using Docker. A GitHub Actions workflow automatically builds the Docker image whenever code is pushed to the repository.

---

## Architecture

Developer
↓
Git Push
↓
GitHub Repository
↓
GitHub Actions
↓
Docker Build
↓
Docker Image
↓
ArgoCD (Concept)
↓
Kubernetes Deployment

---

## Technologies Used

- GitHub
- GitHub Actions
- Docker
- Python Flask
- Kubernetes
- ArgoCD (Concept)

---

## Project Structure

```
Exercise-23-Simple-CICD-Pipeline/
│
├── .github/
│   └── workflows/
│       └── docker.yml
├── argocd/
│   └── application.yaml
├── k8s/
│   └── deployment.yaml
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Steps Performed

1. Created a Flask web application.
2. Added project dependencies.
3. Created a Dockerfile.
4. Built the Docker image.
5. Ran the Docker container locally.
6. Created a Kubernetes Deployment manifest.
7. Created an ArgoCD Application manifest.
8. Configured a GitHub Actions workflow.
9. Pushed the project to GitHub.
10. Verified that the GitHub Actions workflow executed successfully.

---

## Docker Commands

Build Image

```
docker build -t simple-cicd:v1 .
```

Run Container

```
docker run -d -p 5000:5000 --name simple-app simple-cicd:v1
```

Check Running Containers

```
docker ps
```

---

## GitHub Actions

The workflow automatically executes whenever code is pushed to the **main** branch.

Workflow Steps:

- Checkout Source Code
- Set up Docker Buildx
- Login to Docker Hub
- Build Docker Image
- Push Docker Image

---

## Kubernetes

The deployment manifest creates one replica of the application and exposes port 5000 inside the container.

---

## ArgoCD

ArgoCD follows the GitOps approach by continuously monitoring the Git repository and synchronizing Kubernetes resources whenever changes are detected.

---

## Learning Outcomes

- GitHub Repository Management
- Docker Image Creation
- Container Management
- GitHub Actions CI Pipeline
- Kubernetes Deployment Manifest
- ArgoCD GitOps Concept
- SSH Authentication with GitHub
- Basic CI/CD Pipeline Implementation

---

## Result

Successfully implemented a simple CI/CD pipeline using GitHub, Docker, GitHub Actions, Kubernetes manifests, and the ArgoCD deployment concept.
