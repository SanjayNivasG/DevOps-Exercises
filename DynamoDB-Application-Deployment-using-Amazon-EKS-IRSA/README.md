# 🚀 Exercise 24 – DynamoDB Application Deployment using Amazon EKS & IRSA

## 📌 Project Overview

This project demonstrates how to deploy a containerized Python application on Amazon EKS that securely performs CRUD operations on Amazon DynamoDB **without using AWS Access Keys**.

Authentication is implemented using **IAM Roles for Service Accounts (IRSA)**, allowing Kubernetes workloads to securely access AWS services through temporary credentials.

---

## 🏗️ Architecture

```
                +----------------------+
                |      Client          |
                +----------+-----------+
                           |
                     HTTP Request
                           |
                           v
              +------------------------+
              | Kubernetes Service     |
              | (LoadBalancer)         |
              +-----------+------------+
                          |
                          v
             +-------------------------+
             | Customer API Pods       |
             | (Python + Flask)        |
             +-----------+-------------+
                         |
              IAM Role via IRSA
                         |
                         v
              +------------------------+
              | Amazon DynamoDB        |
              | Customers Table        |
              +------------------------+
```

---

## 🎯 Objectives

* Deploy a Python Flask application on Amazon EKS.
* Perform Customer CRUD operations using Amazon DynamoDB.
* Eliminate static AWS credentials.
* Implement secure authentication using IRSA.
* Validate end-to-end communication between EKS and DynamoDB.

---

## 🛠️ Technology Stack

| Technology                            | Purpose                   |
| ------------------------------------- | ------------------------- |
| Amazon EKS                            | Kubernetes Cluster        |
| Kubernetes                            | Container Orchestration   |
| Docker                                | Containerization          |
| Python Flask                          | REST API                  |
| Amazon DynamoDB                       | NoSQL Database            |
| IAM Roles for Service Accounts (IRSA) | Secure AWS Authentication |
| IAM Policy                            | DynamoDB Access Control   |
| Docker Hub                            | Container Registry        |
| kubectl                               | Kubernetes Management     |
| eksctl                                | EKS & IRSA Management     |
| AWS CLI                               | AWS Resource Management   |

---

## 📂 Project Structure

```
Exercise-24-DynamoDB-Application/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── deployment.yaml
├── dynamodb-policy.json
└── README.md
```

---

## 🔐 Security Implementation

Instead of embedding AWS Access Keys inside the application:

* IAM OIDC Provider configured
* IAM Policy created for DynamoDB
* IAM Role attached to Kubernetes Service Account
* Application authenticated using IRSA
* Temporary AWS credentials automatically provided by EKS

**No AWS Access Keys are stored inside the application or container.**

---

## ⚙️ Features

* Create Customer
* Read Customer
* Update Customer
* Secure access to DynamoDB
* Kubernetes Deployment
* LoadBalancer Service
* Dockerized Application
* IRSA Authentication

---

## 🚀 Deployment Workflow

1. Create Amazon EKS Cluster
2. Create DynamoDB Table
3. Configure IAM OIDC Provider
4. Create IAM Policy
5. Create IAM Service Account (IRSA)
6. Build Docker Image
7. Push Image to Docker Hub
8. Deploy Application to EKS
9. Verify CRUD Operations
10. Validate DynamoDB Updates

---

## 📸 Project Verification

### EKS Cluster

* Kubernetes nodes running successfully

### IRSA

* IAM Role attached to Kubernetes Service Account

### DynamoDB

* Customers table created successfully

### Application

* Customer API deployed successfully

### CRUD Validation

✔ Create Customer

✔ Read Customer

✔ Update Customer

✔ Read Updated Customer

---

## 📋 API Endpoints

### Create Customer

```
POST /customer
```

### Read Customer

```
GET /customer/{CustomerId}
```

### Update Customer

```
PUT /customer/{CustomerId}
```

---

## 🧪 Sample Requests

### Create

```bash
curl -X POST http://localhost:8080/customer \
-H "Content-Type: application/json" \
-d '{
  "CustomerId":"101",
  "CustomerName":"Sanjay"
}'
```

### Read

```bash
curl http://localhost:8080/customer/101
```

### Update

```bash
curl -X PUT http://localhost:8080/customer/101 \
-H "Content-Type: application/json" \
-d '{
  "CustomerName":"Nivas"
}'
```

---

## ✅ Key Learning Outcomes

* Amazon EKS Deployment
* Kubernetes Service Accounts
* IAM Roles for Service Accounts (IRSA)
* Amazon DynamoDB Integration
* Docker Image Creation
* Kubernetes Deployments & Services
* Secure AWS Authentication
* Production-oriented Kubernetes Security Practices

---

## 📷 Important Screenshots

* 01-EKS-Nodes.png
* 02-IRSA-ServiceAccount.png
* 03-DynamoDB-Table.png
* 04-Customer-Pods.png
* 05-Service-LoadBalancer.png
* 06-DynamoDB-CRUD-Success.png

---

## 📌 Result

Successfully deployed a secure, containerized customer management application on Amazon EKS with Amazon DynamoDB integration using IAM Roles for Service Accounts (IRSA), demonstrating production-ready authentication without AWS Access Keys.
