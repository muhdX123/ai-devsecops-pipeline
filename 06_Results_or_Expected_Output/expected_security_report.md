# Expected Security Detection Report

## 1. System

**AI-Assisted Web Vulnerability Detection System**

## 2. Detection Summary

| Input ID | Vulnerability Type | Expected Result |
|---|---|---|
| 1 | SQL Injection (SQLi) | Vulnerability Detected |
| 2 | Cross-Site Scripting (XSS) | Vulnerability Detected |
| 3 | Safe Input | No Vulnerability |
| 4 | Safe Input | No Vulnerability |
| 5 | SQL Injection (SQLi) | Vulnerability Detected |
| 6 | Cross-Site Scripting (XSS) | Vulnerability Detected |
| 7 | Safe Input | No Vulnerability |
| 8 | Safe Input | No Vulnerability |

## 3. Expected Classification

The proposed AI model is expected to classify each input into:

1. Safe
2. SQL Injection (SQLi)
3. Cross-Site Scripting (XSS)

## 4. Expected System Behaviour

When a vulnerability is detected, the system is expected to generate a security alert and log the finding.

When no vulnerability is detected, the input is expected to be classified as safe.

The detection results are intended to be passed to the containerized CI/CD pipeline as part of the proposed DevSecOps workflow.
