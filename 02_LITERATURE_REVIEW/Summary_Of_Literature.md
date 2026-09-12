

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

