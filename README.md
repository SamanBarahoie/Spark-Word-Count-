Spark Word Count with Docker and Minikube
Welcome to the Spark Word Count project! This repository demonstrates a robust pipeline for running a PySpark application on Kubernetes using Minikube and Docker. The application processes a text file to count word occurrences, showcasing a scalable, containerized big data workflow orchestrated with the Spark Operator.
📖 Overview
This project implements a simple yet powerful PySpark application that:

Reads a text file (input.txt) containing sample data.
Performs a word count operation using Apache Spark.
Packages the application in a Docker image.
Deploys and runs the job on a Kubernetes cluster managed by Minikube.

The project is designed for DevOps engineers, data engineers, and developers looking to explore containerized Spark workloads in a cloud-native environment.
🎯 Objectives

Demonstrate containerization of a PySpark application with Docker.
Orchestrate Spark jobs on Kubernetes using the Spark Operator.
Provide a reproducible, well-documented workflow for local development and testing.
Showcase best practices for managing Kubernetes resources and debugging.

🛠️ Prerequisites
To run this project, ensure the following tools are installed on your system:

Docker Desktop: For building and managing container images.
Minikube: For running a local Kubernetes cluster.
kubectl: For interacting with Kubernetes.
Helm: For installing the Spark Operator.
Git: For cloning and managing the repository.

Installation Instructions

Docker Desktop: Download and install from docker.com.
Minikube:choco install minikube


kubectl:choco install kubernetes-cli


Helm:choco install kubernetes-helm


Chocolatey (if not installed):Follow instructions at chocolatey.org.

📂 Project Structure
The repository contains the following files:

wordcount.py: The PySpark application that performs word counting.
input.txt: Sample input text file for the word count job.
Dockerfile: Defines the Docker image for the PySpark application.
spark-job.yaml: Kubernetes manifest for the Spark Job.
README.md: This documentation file.

🚀 Getting Started
Follow these steps to set up and run the project on your local machine.
1. Start Minikube
Launch a Minikube cluster with sufficient resources:
minikube start --driver=docker --memory=4096 --cpus=2

2. Build the Docker Image
Build the Docker image in Minikube's Docker environment:
& minikube docker-env | Invoke-Expression
docker build -t spark-wordcount:1.0 .

Verify the image:
docker images | findstr spark-wordcount

3. Install Spark Operator
Add the Spark Operator Helm repository and install it:
helm repo add spark-operator https://kubeflow.github.io/spark-operator
helm repo update
helm install spark-operator spark-operator/spark-operator --namespace spark-operator --create-namespace

Verify the installation:
kubectl get pods -n spark-operator

4. Create Service Account
Set up a Kubernetes Service Account for Spark:
kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default

5. Deploy the Spark Job
Apply the Spark Job manifest:
kubectl apply -f spark-job.yaml

6. Monitor and Verify Output
Check the status of the Pods:
kubectl get pods

View the output in the Driver Pod's logs:
kubectl logs wordcount-job-driver

Expected output:
+-----+-----+
| word|count|
+-----+-----+
|hello|    2|
|world|    1|
|spark|    2|
|  k8s|    1|
+-----+-----+

🧹 Resource Management and Cleanup
Monitoring
Check the status of the Spark Application:
kubectl get sparkapplication

View detailed Pod information:
kubectl describe pod wordcount-job-driver

Cleanup
After the job completes, free up resources:
kubectl delete -f spark-job.yaml

Verify that Pods are removed:
kubectl get pods

🔍 Troubleshooting

Docker Build Fails:
Ensure wordcount.py and input.txt exist in the project directory.
Verify that Docker Desktop is running.


Job Fails to Run:
Check Driver logs: kubectl logs wordcount-job-driver.
Increase Minikube resources: minikube start --memory=6144 --cpus=4.


Spark Operator Issues:
Confirm the operator is running: kubectl get pods -n spark-operator.
Reinstall if needed: helm upgrade --install spark-operator ....



💡 Tips and Best Practices

Save Output: Modify wordcount.py to save results to a file:word_counts.write("/app/output", format="csv", mode="overwrite")

Extract the output:kubectl cp wordcount-job-driver:/app/output <local-path>


Resource Optimization: Adjust cores and memory in spark-job.yaml based on workload.
Re-running Jobs: Re-apply spark-job.yaml to run the job again.
Persistent Images: The spark-wordcount:1.0 image remains in Minikube until manually deleted.

📚 Resources

Spark Operator Documentation
Minikube Documentation
Apache Spark Documentation
Kubernetes Documentation
Helm Documentation

🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.
📬 Contact
For questions or feedback, reach out via GitHub Issues.

Built with ❤️ for the cloud-native data community.
