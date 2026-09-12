

## 2.4 Machine Learning and Deep Learning Techniques for Cross-Site Scripting Detection

Deep learning techniques have similarly been applied to XSS detection.

**Fang et al. (2018)** proposed DeepXSS, which uses word2vec to convert XSS payloads into feature vectors that preserve semantic meaning, followed by a Long Short-Term Memory (LSTM) network for classification. This approach performed well at identifying payloads that had been obfuscated or encoded, a common technique attackers use to bypass rule-based filters.

More recently, **Alhamyani and Alshammari (2024)** compared several machine learning classifiers for XSS detection, including Random Forest and ensemble models, and reported a detection accuracy of 99.78 percent with the Random Forest model while maintaining low false-positive and false-negative rates. Their work confirms that well-tuned classical machine learning models can perform competitively with deep learning approaches.

However, both studies focus on detecting XSS payloads in isolation and do not address how such models could be integrated into an automated build and deployment pipeline.

