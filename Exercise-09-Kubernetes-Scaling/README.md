# Exercise 09 – Kubernetes Deployment Scaling

## Objective

Learn how to scale a Kubernetes Deployment using `kubectl`.

## Tools Used

* Ubuntu 24.04
* Docker
* Minikube
* Kubernetes (kubectl)

## Steps Performed

1. Started Minikube.
2. Created an Nginx Deployment.
3. Verified the Deployment.
4. Scaled the Deployment from 1 replica to 3 replicas.
5. Verified that three Pods were running.
6. Scaled the Deployment back to 1 replica.
7. Verified that one Pod was running.

## Commands Used

```bash
minikube start --driver=docker --memory=2048 --cpus=2

kubectl create deployment nginx-app --image=nginx

kubectl get deployments

kubectl get pods

kubectl scale deployment nginx-app --replicas=3

kubectl get pods

kubectl scale deployment nginx-app --replicas=1

kubectl get pods
```

## Output

* Deployment created successfully.
* Deployment scaled to **3 replicas**.
* Deployment scaled back to **1 replica**.

## Screenshots

* Deployment Scaled to 3 Replicas
* Deployment Scaled Back to 1 Replica

## Learning Outcome

* Understood Kubernetes Deployments.
* Learned how to scale applications using `kubectl scale`.
* Verified replica changes using `kubectl get pods`.
* Gained hands-on experience with Kubernetes scaling operations.
