# Chapter 2 — Literature Review

## Introduction

This chapter reviews existing research related to automated security testing, machine learning-based vulnerability detection and the use of Artificial Intelligence (AI) within DevSecOps pipelines.

The review is organised into four main sub-topics:

1. **Deep Learning Approaches for Source Code Vulnerability Detection**
2. **Machine Learning and Deep Learning Techniques for SQL Injection Detection**
3. **Machine Learning and Deep Learning Techniques for Cross-Site Scripting Detection**
4. **AI-Assisted Security Testing in DevSecOps and CI/CD Pipelines**

A summary table is included, followed by the research gap analysis.

## 2.2 Deep Learning Approaches for Source Code Vulnerability Detection

Several studies have applied deep learning to detect vulnerabilities directly from source code instead of relying on predefined rules.

**Li et al. (2018)** proposed VulDeePecker, a system that extracts code gadgets from program slices and trains a Bidirectional Long Short-Term Memory (BLSTM) network to classify vulnerable code patterns. The system achieved higher detection accuracy than conventional static analysis tools on buffer error and resource management vulnerabilities. However, VulDeePecker represents code as flat token sequences, which loses structural information such as control flow and data dependency, limiting its ability to capture more complex vulnerability patterns.

**Zhou et al. (2019)** addressed this limitation with Devign, a model that represents each function as a composite graph combining the abstract syntax tree, control flow graph, data flow graph and natural code sequence. A gated graph recurrent network was used to learn from this composite graph, allowing the model to capture richer program semantics than sequence-based models. Devign outperformed prior methods by 10.51 percent in accuracy and 8.68 percent in F1-score on real-world C projects. Although this demonstrates that structural representation improves detection accuracy, the additional graph construction and training overhead is a concern for lightweight inference within time-constrained CI/CD pipelines.

## 2.3 Machine Learning and Deep Learning Techniques for SQL Injection Detection

Static analysis methods that compare the structure of dynamically generated queries against a predefined model have also been used to detect SQLi.

**Yuan et al. (2023)** proposed a static detection method based on program transformation, in which object-oriented database code is converted into equivalent procedural code and then analysed using control flow graphs. This method allows SQLi vulnerabilities to be detected in code that is not directly written as raw SQL queries, but it depends on the accuracy of the code transformation stage and may not generalise well to languages that were not covered during the transformation design.

**Arasteh et al. (2024)** proposed a feature selection approach using two binary versions of the Gray Wolf Optimizer to reduce a thirteen-feature SQLi dataset to its most informative subset before classification. The resulting model achieved 99.68 percent accuracy while using only 20 percent of the original features, showing that feature selection can reduce computational cost without reducing detection performance.

Similarly, **Ross (2018)** combined multiple data sources, including network traffic and application logs, with machine learning classifiers to detect SQLi attacks, and found that combining data sources improved detection reliability compared to relying on a single source. However, both studies were evaluated on datasets generated in controlled environments, so their performance on live, evolving web traffic inside a real CI/CD pipeline remains uncertain.

## 2.4 Machine Learning and Deep Learning Techniques for Cross-Site Scripting Detection

Deep learning techniques have similarly been applied to XSS detection.

**Fang et al. (2018)** proposed DeepXSS, which uses word2vec to convert XSS payloads into feature vectors that preserve semantic meaning, followed by a Long Short-Term Memory (LSTM) network for classification. This approach performed well at identifying payloads that had been obfuscated or encoded, a common technique attackers use to bypass rule-based filters.

More recently, **Alhamyani and Alshammari (2024)** compared several machine learning classifiers for XSS detection, including Random Forest and ensemble models, and reported a detection accuracy of 99.78 percent with the Random Forest model while maintaining low false-positive and false-negative rates. Their work confirms that well-tuned classical machine learning models can perform competitively with deep learning approaches.

However, both studies focus on detecting XSS payloads in isolation and do not address how such models could be integrated into an automated build and deployment pipeline.

## 2.5 AI-Assisted Security Testing in DevSecOps and CI/CD Pipelines

A smaller number of studies have examined how AI techniques can be embedded directly into DevSecOps workflows.

**Bedoya et al. (2024)** proposed integrating a Large Language Model into the design stage of the software development lifecycle to support automated threat discovery, combined with Security Chaos Engineering to identify flaws that conventional security tools may miss. Their case study, applied to a retail company, demonstrated that combining AI-based threat discovery with proactive security testing can reduce the number of vulnerabilities that reach later stages of development.

However, the proposed approach targets threat discovery at the design stage rather than continuous, automated scanning of source code and HTTP traffic during the CI/CD build and deployment process, which is the specific direction of the proposed study.

## 2.6 Summary of Reviewed Literature

| Study | Method / Technique | Key Finding | Limitation Identified |
|---|---|---|---|
| Li et al. (2018) | BLSTM on code gadgets extracted from program slices (VulDeePecker) | Achieved higher detection accuracy than conventional static analyzers on buffer and resource-management vulnerabilities | Treats code as flat token sequences; loses control-flow and data-dependency structure |
| Zhou et al. (2019) | Composite code graph (AST, CFG, DFG, code sequence) with a gated graph recurrent network (Devign) | Outperformed sequence-based models by 10.51% accuracy and 8.68% F1-score on real-world C projects | Higher computational overhead, which is a concern for time-constrained CI/CD execution |
| Yuan et al. (2023) | Static detection via program transformation and control-flow-graph analysis for SQL Injection | Detected SQLi vulnerabilities in object-oriented database code not written as raw SQL | Depends on accurate code transformation; limited generalisability across languages |
| Arasteh et al. (2024) | Binary Gray Wolf Optimizer for feature selection combined with ML classifiers for SQLi detection | 99.68% accuracy using only 20% of the original 13 features | Evaluated on a controlled dataset; live, evolving web traffic not tested |
| Ross (2018) | ML classifiers trained on multiple data sources (network traffic and application logs) for SQLi | Combining data sources improved detection reliability over a single source | Dataset generated in a controlled test environment rather than production traffic |
| Fang et al. (2018) | word2vec feature embedding with LSTM classification for XSS payloads (DeepXSS) | Effective at identifying obfuscated or encoded payloads used to bypass rule-based filters | Focuses on payload classification only; no pipeline integration discussed |
| Alhamyani & Alshammari (2024) | Comparison of ML classifiers (Random Forest, ensemble models) for XSS detection | Random Forest achieved 99.78% accuracy with low false-positive and false-negative rates | Detects XSS in isolation; does not address SQLi or pipeline deployment |
| Bedoya et al. (2024) | Large Language Model for design-stage threat discovery combined with Security Chaos Engineering | Reduced vulnerabilities reaching later development stages in a retail case study | Targets design-stage discovery, not continuous automated scanning during CI/CD execution |

## 2.7 Research Gap

The reviewed studies show that static, context-limited detection methods and AI-based detection methods have both been researched extensively for SQLi and XSS individually.

Deep learning models such as **VulDeePecker** and **Devign** demonstrate that learning from code structure improves detection accuracy, but neither was evaluated within an automated CI/CD execution context, and their computational cost may not suit lightweight pipeline inference.

SQLi- and XSS-specific studies, such as those by **Arasteh et al. (2024), Ross (2018), Fang et al. (2018)** and **Alhamyani and Alshammari (2024)**, report strong detection performance, but each targets a single vulnerability type in isolation, using datasets collected outside a live pipeline environment.

Studies that examine AI integration within DevSecOps, such as **Bedoya et al. (2024)**, focus on design-stage threat discovery rather than runtime detection embedded directly into the build and deployment process.

### Main Research Gap

Overall, no reviewed study presents a lightweight AI-assisted detection model that jointly addresses:

- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- detection within **source code and HTTP request parameters**
- evaluation inside a **containerized CI/CD pipeline**
- **detection accuracy**
- **false-positive rate**
- **execution time**

This research addresses that gap by designing and evaluating an AI-assisted vulnerability detection prototype for integration into a DevSecOps pipeline.

## Chapter 2 Summary

The literature indicates that AI and machine learning can improve vulnerability detection through learned representations, feature selection and semantic analysis. Deep learning approaches can capture complex code characteristics, while traditional machine learning models can also achieve strong results for specific web vulnerabilities.

However, existing research commonly evaluates SQLi, XSS or source-code vulnerability detection separately and often uses controlled datasets or environments outside continuous CI/CD execution. DevSecOps-related work has also focused more on design-stage threat discovery than on lightweight runtime vulnerability detection inside the build and deployment pipeline.

These limitations support the proposed direction of an AI-assisted vulnerability detection prototype that combines selected SQLi and XSS detection capabilities with containerized CI/CD execution.

## References

Alhamyani, R., & Alshammari, M. (2024). Machine learning-driven detection of cross-site scripting attacks. *Information, 15*(7), 420. https://doi.org/10.3390/info15070420

Arasteh, B., Aghaei, B., Farzad, B., Arasteh, K., Kiani, F., & Torkamanian-Afshar, M. (2024). Detecting SQL injection attacks by binary gray wolf optimizer and machine learning algorithms. *Neural Computing and Applications, 36*(12), 6771–6792. https://doi.org/10.1007/s00521-024-09429-z

Bedoya, M., Palacios, S., Díaz-López, D., Laverde, E., & Nespoli, P. (2024). Enhancing DevSecOps practice with large language models and security chaos engineering. *International Journal of Information Security, 23*(6), 3765–3788. https://doi.org/10.1007/S10207-024-00909-W

Fang, Y., Li, Y., Liu, L., & Huang, C. (2018). DeepXSS: Cross site scripting detection based on deep learning. In *Proceedings of the 2018 International Conference on Computing and Artificial Intelligence* (pp. 47–51).

Li, Z., Zou, D., Xu, S., Ou, X., Jin, H., Wang, S., Deng, Z., & Zhong, Y. (2018). VulDeePecker: A deep learning-based system for vulnerability detection. In *Proceedings of the 25th Network and Distributed System Security Symposium (NDSS)*.

Ross, K. (2018). *SQL injection detection using machine learning techniques and multiple data sources* [Master's thesis, San José State University]. SJSU ScholarWorks.

Yuan, Y., Lu, Y., Zhu, K., Huang, H., Yu, L., & Zhao, J. (2023). A static detection method for SQL injection vulnerability based on program transformation. *Applied Sciences, 13*(21), 11763. https://doi.org/10.3390/app132111763

Zhou, Y., Liu, S., Siow, J., Du, X., & Liu, Y. (2019). Devign: Effective vulnerability identification by learning comprehensive program semantics via graph neural networks. In *Advances in Neural Information Processing Systems (NeurIPS 32)*.
