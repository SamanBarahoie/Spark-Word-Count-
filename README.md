
# 🚀 Spark Word Count with Docker and Minikube

Welcome to the **Spark Word Count** project! This repository demonstrates a robust pipeline for running a PySpark application on Kubernetes using Minikube and Docker. It processes a text file to count word occurrences—showcasing a scalable, containerized big data workflow orchestrated with the Spark Operator.

---

## 📖 Overview

This project implements a simple yet powerful PySpark application that:

- Reads a text file (`input.txt`) containing sample data.
- Performs a word count operation using Apache Spark.
- Packages the application in a Docker image.
- Deploys and runs the job on a Kubernetes cluster managed by Minikube.

**Target Audience:** DevOps engineers, data engineers, and developers exploring containerized Spark workloads in a cloud-native environment.

---

## 🎯 Objectives

- ✅ Containerize a PySpark application with Docker.
- ✅ Orchestrate Spark jobs on Kubernetes using the Spark Operator.
- ✅ Provide a reproducible, well-documented workflow.
- ✅ Showcase best practices in managing Kubernetes resources and debugging.

---

## 🛠️ Prerequisites

Ensure the following tools are installed:

- [Docker Desktop](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/)  
  `choco install minikube`
- [kubectl](https://kubernetes.io/docs/tasks/tools/)  
  `choco install kubernetes-cli`
- [Helm](https://helm.sh/)  
  `choco install kubernetes-helm`
- [Git](https://git-scm.com/)

If Chocolatey is not installed, follow instructions at [chocolatey.org](https://chocolatey.org/install).

---

## 📂 Project Structure

```plaintext
.
├── Dockerfile             # Docker image definition for the app
├── input.txt              # Sample input text file
├── spark-job.yaml         # Kubernetes manifest for Spark job
├── wordcount.py           # PySpark application
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### 1. Start Minikube

```bash
minikube start --driver=docker --memory=4096 --cpus=2
```

### 2. Build the Docker Image

Use Minikube’s Docker environment:

```powershell
& minikube docker-env | Invoke-Expression
docker build -t spark-wordcount:1.0 .
docker images | findstr spark-wordcount
```

### 3. Install Spark Operator

```bash
helm repo add spark-operator https://kubeflow.github.io/spark-operator
helm repo update
helm install spark-operator spark-operator/spark-operator \
  --namespace spark-operator --create-namespace
kubectl get pods -n spark-operator
```

### 4. Create Service Account

```bash
kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role \
  --clusterrole=edit \
  --serviceaccount=default:spark \
  --namespace=default
```

### 5. Deploy the Spark Job

```bash
kubectl apply -f spark-job.yaml
```

### 6. Monitor and Verify Output

```bash
kubectl get pods
kubectl logs wordcount-job-driver
```

**Expected Output:**
```
+-----+-----+
| word|count|
+-----+-----+
|hello|    2|
|world|    1|
|spark|    2|
|  k8s|    1|
+-----+-----+
```

---

## 🧹 Resource Management and Cleanup

### Monitoring

```bash
kubectl get sparkapplication
kubectl describe pod wordcount-job-driver
```

### Cleanup

```bash
kubectl delete -f spark-job.yaml
kubectl get pods
```

---

## 🔍 Troubleshooting

**Docker Build Fails:**
- Ensure `wordcount.py` and `input.txt` are present.
- Verify Docker Desktop is running.

**Job Fails to Run:**
- Check Driver logs:
  ```bash
  kubectl logs wordcount-job-driver
  ```
- Increase Minikube resources:
  ```bash
  minikube start --memory=6144 --cpus=4
  ```

**Spark Operator Issues:**
- Confirm it’s running:
  ```bash
  kubectl get pods -n spark-operator
  ```
- Reinstall if needed:
  ```bash
  helm upgrade --install spark-operator ...
  ```

---

## 💡 Tips and Best Practices

- **Save Output:** Modify `wordcount.py` to save results:
  ```python
  word_counts.write.format("csv").mode("overwrite").save("/app/output")
  ```
- **Extract Output Locally:**
  ```bash
  kubectl cp wordcount-job-driver:/app/output <local-path>
  ```
- **Resource Optimization:** Tune resources in `spark-job.yaml`.
- **Re-run Jobs:** Just re-apply `spark-job.yaml`.

---

## 📚 Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/)
- [Spark Operator Docs](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📬 Contact

For questions or feedback, please open a GitHub Issue.

---

Built with ❤️ for the cloud-native data community.
```

