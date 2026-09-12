



## 2.3 Machine Learning and Deep Learning Techniques for SQL Injection Detection

Static analysis methods that compare the structure of dynamically generated queries against a predefined model have also been used to detect SQLi.

**Yuan et al. (2023)** proposed a static detection method based on program transformation, in which object-oriented database code is converted into equivalent procedural code and then analysed using control flow graphs. This method allows SQLi vulnerabilities to be detected in code that is not directly written as raw SQL queries, but it depends on the accuracy of the code transformation stage and may not generalise well to languages that were not covered during the transformation design.

**Arasteh et al. (2024)** proposed a feature selection approach using two binary versions of the Gray Wolf Optimizer to reduce a thirteen-feature SQLi dataset to its most informative subset before classification. The resulting model achieved 99.68 percent accuracy while using only 20 percent of the original features, showing that feature selection can reduce computational cost without reducing detection performance.

Similarly, **Ross (2018)** combined multiple data sources, including network traffic and application logs, with machine learning classifiers to detect SQLi attacks, and found that combining data sources improved detection reliability compared to relying on a single source. However, both studies were evaluated on datasets generated in controlled environments, so their performance on live, evolving web traffic inside a real CI/CD pipeline remains uncertain.

