

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

