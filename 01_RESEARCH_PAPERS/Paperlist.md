# Research Papers for SQL Injection and XSS Detection

This document lists the key research papers used to support the Literature Review (Chapter 2) of the Research Proposal.

---

## Paper 1

| **Item** | **Details** |
|---|---|
| **Paper Title** | VulDeePecker: A Deep Learning-Based System for Vulnerability Detection |
| **Author(s)** | Li, Z., Zou, D., Xu, S., Ou, X., Jin, H., Wang, S., Deng, Z., & Zhong, Y. |
| **Year** | 2018 |
| **Research Problem** | Detecting software vulnerabilities using deep learning on code gadgets |
| **Method / Technique** | Bidirectional Long Short-Term Memory (BLSTM) |
| **Dataset / Tools** | C/C++ program slices (code gadgets) |
| **Main Findings** | Achieved high accuracy on buffer-related vulnerabilities, outperforming static analyzers |
| **Limitation** | Loses control-flow structure since it relies on flat token sequences |
| **Relevance to Proposed Research** | Shows the limits of sequence-only models, supporting our need for structure-aware and lightweight feature representation |

---

## Paper 2

| **Item** | **Details** |
|---|---|
| **Paper Title** | Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks |
| **Author(s)** | Zhou, Y., Liu, S., Siow, J., Du, X., & Liu, Y. |
| **Year** | 2019 |
| **Research Problem** | Improving vulnerability identification by capturing richer program semantics |
| **Method / Technique** | Composite code graph combined with the Devign graph neural network model |
| **Dataset / Tools** | Real-world C projects |
| **Main Findings** | Outperformed sequence-based models by 10.51% in accuracy |
| **Limitation** | High computational overhead; unsuitable for fast CI/CD pipelines |
| **Relevance to Proposed Research** | Confirms the accuracy-speed trade-off our lightweight model must balance for CI/CD integration |

---

## Paper 3

| **Item** | **Details** |
|---|---|
| **Paper Title** | Detection of SQL Injection Attacks Using Gray Wolf Optimizer and Machine Learning Classifiers |
| **Author(s)** | Arasteh, B., et al. |
| **Year** | 2024 |
| **Research Problem** | Improving SQL Injection detection accuracy through optimized feature selection |
| **Method / Technique** | Gray Wolf Optimizer combined with machine learning classifiers |
| **Dataset / Tools** | 13-feature SQLi dataset |
| **Main Findings** | Achieved 99.68% SQLi detection accuracy |
| **Limitation** | Tested only in a controlled environment; isolated to SQLi, no CI/CD context |
| **Relevance to Proposed Research** | Demonstrates strong achievable accuracy for SQLi alone, supporting our choice of ML-based feature-driven detection |

---

## Paper 4

| **Item** | **Details** |
|---|---|
| **Paper Title** | Cross-Site Scripting (XSS) Detection Using Random Forest Classifier |
| **Author(s)** | Alhamyani, R., et al. |
| **Year** | 2024 |
| **Research Problem** | Detecting XSS payloads through supervised classification |
| **Method / Technique** | Random Forest Classifier |
| **Dataset / Tools** | XSS payload datasets |
| **Main Findings** | Achieved 99.78% XSS detection accuracy |
| **Limitation** | Isolated testing; lacks CI/CD pipeline integration |
| **Relevance to Proposed Research** | Confirms Random Forest as a strong, lightweight candidate for XSS detection, supporting a joint SQLi and XSS ensemble approach |
