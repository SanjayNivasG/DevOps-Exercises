#Kubernetes Node NotReady (DiskPressure)

## Objective

Learn how to investigate a Kubernetes node that becomes **NotReady** because of disk space issues.

## Incident

A production Kubernetes node reported:

* Node Status: NotReady
* DiskPressure=True
* Kubelet log: no space left on device

## Investigation

The following commands were used to investigate the issue:

```bash
kubectl get nodes
kubectl describe node minikube
df -h
sudo du -xh / --max-depth=1 | sort -h
docker system df
```

## Root Cause

When the node runs out of disk space, Kubernetes sets **DiskPressure=True** and may mark the node as **NotReady** to protect the cluster.

## Recovery Steps

1. Check node status.
2. Verify disk usage.
3. Find large files or directories.
4. Remove unnecessary logs or unused Docker data.
5. Restart kubelet if required.
6. Verify the node returns to the Ready state.

## Screenshots

* kubectl get nodes
* kubectl describe node
* df -h
* Disk usage analysis
* Docker storage usage

## Outcome

This exercise demonstrates the investigation and recovery process for a Kubernetes Node NotReady incident caused by disk space exhaustion.
