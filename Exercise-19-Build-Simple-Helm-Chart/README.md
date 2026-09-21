# Exercise 19 - Build a Simple Helm Chart

## Overview

This project demonstrates the basics of Helm, the package manager for Kubernetes. The exercise covers creating a Helm chart, deploying an application, verifying Kubernetes resources, upgrading the deployment, and removing the release.

## Objective

* Learn Helm chart structure.
* Deploy an application using Helm.
* Understand the Helm release lifecycle.
* Practice common Helm commands used in DevOps.

## Environment

* Ubuntu EC2 Instance
* Minikube
* Kubernetes
* Helm

## Project Structure

```
Exercise-19-Build-Simple-Helm-Chart/
│
├── myapp/
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── templates/
│   └── charts/
│
├── screenshots/
│
└── README.md
```

## Steps Performed

### 1. Created a Helm Chart

Created a new Helm chart using:

```bash
helm create myapp
```

This generated the default Helm chart structure with templates and configuration files.

### 2. Installed the Chart

Installed the application into the Kubernetes cluster.

```bash
helm install my-release ./myapp
```

Verified the deployment using:

```bash
helm list
kubectl get all
```

### 3. Upgraded the Release

Updated the existing Helm release.

```bash
helm upgrade my-release ./myapp
```

### 4. Uninstalled the Release

Removed the deployed application from the cluster.

```bash
helm uninstall my-release
```

Verified that all application resources were removed.

## Helm Commands Used

```bash
helm create myapp
helm install my-release ./myapp
helm list
helm upgrade my-release ./myapp
helm uninstall my-release
kubectl get all
```

## Screenshots

* Helm chart directory structure
* Successful Helm installation
* Kubernetes resources after deployment
* Helm upgrade
* Successful Helm uninstall

## Key Learnings

* Helm simplifies Kubernetes application deployment.
* A Helm chart contains reusable Kubernetes templates.
* A Helm release is a deployed instance of a chart.
* `helm install` creates a new release.
* `helm upgrade` updates an existing release.
* `helm uninstall` removes the deployed application.

## Outcome

Successfully created a Helm chart, deployed it to a Kubernetes cluster, verified the resources, upgraded the release, and removed it using Helm commands.
