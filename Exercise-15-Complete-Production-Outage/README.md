# Exercise 15 – Complete Production Outage

## Overview

This exercise simulates a real production outage where an application started returning **HTTP 503 Service Unavailable** errors after a deployment. Although the Kubernetes infrastructure appeared healthy, the application could not connect to Redis because of a secret synchronization issue.

The objective was to investigate the incident, identify the root cause, restore the service, and recommend preventive measures.

---

## Scenario

* Secret Manager rotated the Redis password at **08:55 AM**.
* Application deployment completed successfully at **09:00 AM**.
* At **09:05 AM**, users started receiving **HTTP 503** errors.

During the investigation:

* ArgoCD showed **Healthy**.
* Kubernetes Pods were **Running**.
* Ingress was **Healthy**.
* Application logs showed **Cannot connect to Redis**.
* Redis logs showed **Authentication failed**.

---

## Investigation Process

### Step 1 – Verify ArgoCD

Checked the application status in ArgoCD to ensure the deployment was successful and synchronized.

Result:

* Application was Healthy.
* No deployment issues were found.

---

### Step 2 – Verify Kubernetes Pods

Checked all application pods.

Result:

* All pods were running successfully.
* No pod crashes or restart issues were found.

---

### Step 3 – Verify Ingress

Checked the Ingress resource.

Result:

* Ingress was healthy.
* Network routing was working correctly.

---

### Step 4 – Check Application Logs

Reviewed application logs.

Found:

Cannot connect to Redis

This confirmed that the application was unable to establish a connection with Redis.

---

### Step 5 – Check Redis Logs

Reviewed Redis logs.

Found:

Authentication failed

This indicated that Redis was rejecting the application's credentials.

---

### Step 6 – Verify Secret Synchronization

Compared the Secret Manager value with the Kubernetes Secret.

Found:

* Redis password had been rotated.
* Kubernetes Secret still contained the old password.
* External Secret had not synchronized the updated value.

---

## Root Cause

The Redis password was rotated in Secret Manager before the deployment.

However, the updated password was not synchronized to the Kubernetes Secret.

As a result:

* The application continued using the old Redis password.
* Redis rejected the authentication request.
* The application could not establish a connection.
* Users received HTTP 503 responses.

---

## Immediate Resolution

The following actions were taken:

* Refreshed the External Secret.
* Verified that the Kubernetes Secret contained the updated password.
* Restarted the application deployment.
* Confirmed that the application successfully connected to Redis.

---

## Long-Term Prevention

* Enable automatic synchronization for External Secrets.
* Restart applications after secret rotation.
* Validate secret versions before deployment.
* Implement automated health checks after deployments.
* Include secret verification in the deployment pipeline.

---

## Monitoring Improvements

The following alerts should be configured:

* Secret synchronization failures
* Redis authentication failures
* Application connection failures
* Secret expiration alerts
* HTTP 503 error rate alerts

---

## Skills Practiced

* Production Incident Investigation
* Root Cause Analysis (RCA)
* Kubernetes Troubleshooting
* Secret Management
* External Secrets
* Redis Authentication
* Application Log Analysis
* Production Monitoring
* Incident Documentation

---

## Key Learning

This exercise demonstrates that a healthy Kubernetes cluster does not always mean the application is healthy. Even when ArgoCD, Pods, and Ingress report healthy status, application-level dependencies such as Redis and Secrets must also be verified during incident investigation.
