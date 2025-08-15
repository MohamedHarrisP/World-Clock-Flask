# World-Clock-Flask

This is a World Clock application developed using Flask. The primary objective of this project is not to develop a clock application, but to practically learn building in security to a Flask application, as part of the Software Development Lifecycle (SDLC). Building in security as early in the SDLC is a good practice as it reduces the time and cost in addressing vulnerabilities, if they are found after deployment. This project demonstrates the Shift Left behavious, a DevSecOps methodology which advocates performing security scanning as the code is being built and remediating vulnerabilities before the code is deployed.

# Project Structure:
The folder 'app' has two files,
- main.py: The Python code for the application
- index.html: The HTML part of this application

I intend this application to be a containerized one. The Dockerfile can be found in the repo which is used to build the image.

# Project Flow
The ci-cd-pipeline.yml file which can be found in .github/workflows has the following steps,
  - Static Application Security Testing using Semgrep to identify vulnerabilities in the code
  - Software Composition Analysis using pip-audit to identify vulnerable third-party dependencies used by this app
  - Secrets Scanning using Gitleaks to detect any hard-coded secrets in the code
  - Building Image using the instructions given in the Dockerfile
  - Image Scanning using Trivy to detect vulnerabilities in the image built in the previous step
  - Uploading the image to AWS Elastic Container Registry

By running the GitHub Actions file, all of the above steps are automatically performed. Every time the image is uploaded to AWS ECR, it is tagged accordingly.

I've used a free-tier account in AWS to demonstrate the usage of ECR. In order to use this code, you may need an AWS account and complete the following steps.

- Create a registry in ECR
- Create an IAM user and give push permissions to the repository
- Copy the AWS Access ID and Secret Access Key and add those secrets in GitHub Secrets
- Execute the GitHub Actions file

Please connect with me, if you've any thoughts to share on this project. Looking forward to collaborate!
