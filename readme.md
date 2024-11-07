# Data Flow

![https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Workflow.png](https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Workflow.png)

---

This system focuses on the development of a data pipeline 🔧🔨 to extract, transform, and load **(ETL)** data from a hosted source into our inhouse database.

The ETL process will involve extracting relevant data from the source database using Python 🐍🐍 APIs, transforming the data to align with the database schema and loading the transformed data into our target infrastructure 📦📦.

The data pipeline will be designed to be scalable, efficient, and reliable, ensuring timely ⌚⌚ and accurate data integration. Additionally, we will implement error handling and logging mechanisms to monitor the pipeline's performance and troubleshoot any issues.

---

### Tools and Skills in this Project :

✅ Docker Images and Containerization

✅ Apache Airflow for data systems orchestration

✅ Python scripting 

✅ Basic Linux knowledge

![icons8_Python_1.svg](icons8_Python_1.svg)

![icons8_Docker.svg](icons8_Docker.svg)

![icons8_no_linux_2.svg](icons8_no_linux_2.svg)

![icons8_Bash.svg](icons8_Bash.svg)

---

### This is how we’ll do it 🔥🔥:

1. Configure our environment and install our libraries. A docker container will host all out codes.
2. Code the algorithm to extract the data from the hosted database and loads into our landing zone
3. Write algorithms to transform this data and load to our staging zone
4. Write a schema that matches our inhouse database
5. Load the data onto our database

---

## Let’s Get into it

Ensure You have docker installed in you system. You can find installation instructions in the link. [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/) 

Then run the following series of commands to configure our environment.

### 1. Configure Docker

```bash
# Pull the docker image 
docker pull allanmogley/arcgis:latest
```

### 2. Install and Configure Apache Airflow

Find Complete Installation Guide Here: [https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)

```bash
# Install Apache Airflow
pip install "apache-airflow[celery]==2.10.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.8.txt"

# Install docker airflow provider
pip install apache-airflow-providers-docker
```