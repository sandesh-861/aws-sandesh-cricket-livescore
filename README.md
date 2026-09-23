# 🏏 AWS Serverless Live Cricket Scoreboard

A responsive live cricket scoreboard web application deployed serverless on Amazon Web Services (AWS).

## 🌐 Live Demo
🔗 [View Live Application](http://sandesh-cricket-live-2026.s3-website.ap-south-1.amazonaws.com)

---

## 🏗️ Architecture
* **Frontend:** Hosted via **Amazon S3** Static Website Hosting
* **API Layer:** **Amazon API Gateway** (REST API)
* **Compute:** **AWS Lambda** (Python / Node.js) to serve match data
* **Version Control:** Git & GitHub

---

## 🚀 Deployment Steps
1. Configured an S3 bucket with public read policy for static hosting.
2. Built a Lambda function returning match payload with CORS enabled.
3. Created an API Gateway HTTP trigger to bridge frontend requests to Lambda.
4. Uploaded frontend static assets and version-controlled via GitHub.
