# Expected Evaluation Metrics

The proposed system will be evaluated using the following metrics.

## 1. Detection Accuracy

Detection accuracy measures how correctly the system classifies inputs as Safe, SQL Injection (SQLi), or Cross-Site Scripting (XSS).

Accuracy = (Correct Predictions / Total Predictions) × 100%

## 2. False-Positive Rate

False-positive rate measures how often safe inputs are incorrectly classified as vulnerabilities.

False-Positive Rate = FP / (FP + TN) × 100%

## 3. Detection Time

Detection time measures the time required by the system to process and classify an input.

## 4. CI/CD Integration

The prototype is expected to operate within a containerized CI/CD environment and generate a security report or alert based on the detection result.

## Expected Outcome

The proposed system is expected to provide accurate detection of SQL Injection and Cross-Site Scripting, reduce false-positive results, and perform detection within a reasonable time for integration into a CI/CD pipeline.

Note:
These are expected evaluation criteria, not actual experimental results. Actual accuracy, false-positive rate, and detection time should only be reported after the prototype has been implemented and tested.
