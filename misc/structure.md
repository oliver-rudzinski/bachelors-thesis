# Thesis Structure `WiP`

1. **Introduction**
   - Motivation
   - Relation to Project Environment
   - Scope within superordinate Project
   - Task Definition
   - Chapter Overview
2. **Theoretical Backgrounds**
   - Introduction to DataOps
     - Limitations of Traditional Approach
     - Move to Agile Approach
     - Value and Innovation Pipelines
     - Environments
     - Self-containment of individual solution parts
   - Introduction to Testing
     - Integrity Requirements of Data Analytics Solutions
     - Testing Domains
     - Excursus to Software Testing, Differences to Data Testing
   - Technical Fundamentals
     - GitHub (advanced features)
     - Airflow
     - Jenkins
     - Virtual Containers (Docker)
     - AWS (EC2, S3, ECR, ECS, Athena)
     - (Python and PyTest as part of the solution)
3. **Analytics Pipeline DataOps Enablement**
   - Target-Performance Analysis → Requirements for DataOps Enablement
   - Architecture Design
     - Containerization of Data Pipeline Components
     - CI/CD Pipeline Definitions (Testing Placeholder)
     - Environment Definitions
       - Jenkins & GitHub (master, develop, feature/*)
       - S3 (Test Data vs. Real Data), Access Control, Sensitive Data Protection
     - Deployment Strategy (Jenkins → ECR → ECS)
   - Modus Operandi: Change in Dev Sandbox → Commit to specific feature branch → Pull Request → Automatic Recognition in Build Pipeline → Build, Test, and Deployment Process → on pass: Change in Production
   - Implementation
4. **DataOps Testing (`convert` & `sanitize` stage)**
   - Testing Strategy
     - Pathological Data Sets
     - `convert` Input Data:
       - Schema Tests (Attributes)
       - Validity Tests (Values)
       - Data Quality Tests (Percentage of valid files, definition of thresholds)
       - Smoke Tests (Essential attributes & values processable by transformation)
     - `convert` Data Transformation
       - Unit Testing: Do the performed transformations of valid input data result in the expected output
     - `convert` Output Data (== `sanitize` Input Data)
       - Schema Tests, Validity Tests, Data Quality Tests, Smoke Tests based on previously generated data
   - Technical Testing Architecture
     - Event definitions for `convert` and `sanitize`, custom Exceptions, variable threshold acceptance
     - stage-specific testing
     - End-to-End testing (first stage receives prod-grade input data, runs through all stages, MBA is checked for validity)
     - Testing Embedding in Build Pipeline
   - Implementation
5. **Solution Evaluation** `WiP`
   - Performance?
   - Loopholes?
   - Edge Cases?
6. **Conclusion**
   - Perceived vs. actual value for department
   - Further research
   - Summary
