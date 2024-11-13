
---

# Data Flow

![https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Workflow.png](https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Workflow.png)

---

This system focuses on the development of a data pipeline 🔧🔨 to extract, transform, and load **(ETL)** data from a hosted source into our inhouse database.

The ETL process extracts raw data from the source database using ArcGIS Python 🐍🐍 APIs, process and transform the data to our inhouse database schema and load the transformed data into our target infrastructure 📦📦.

---

# Part One

Build and Test the data pipeline on a local environment.

## Tools :

✅ Docker Images and Containerization

✅ Apache Airflow for data systems orchestration

✅ Python scripting 

✅ Basic Linux knowledge



---

## Let’s Get into it 🚀🚀

Ensure You have docker installed in you system. You can find installation instructions in the link. [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/) 

Then run the following series of commands to configure our environment.

### 1. Configure Docker

```bash
# Pull the docker image 
# This image alreadly contains the python scripts
docker pull allanmogley/arcgis:latest
```

### 2. Install and Configure Apache Airflow

Find Complete Installation Guide Here:

[https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)

```bash
# Install Apache Airflow
pip install "apache-airflow[celery]==2.10.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.8.txt"

# Install docker airflow provider
pip install apache-airflow-providers-docker
```

3. ### Create an Airflow DAG

   Create a dataflow.py file inside airflow/dags folder.

```bash
# -----------------------
# Bash
# -----------------------

touch airflow/dags/dataflow.py
```

![https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Directories.png](https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/Directories.png)

​	Paste the following code into the dataflow.py file

```python
# -----------------------
# Python Script
# -----------------------

from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

# Create dag
with DAG('dataflow',
         start_date = datetime.now(),
         schedule = '*/5 * * * *',
         max_active_runs = 1
         ) as dag:
	
    # Data Extactor Task
    # Runs within the docker image
    extract = DockerOperator(
            task_id = 'extract_data',
            image = 'allanmogley/arcgis:latest',
            auto_remove = 'never',
            container_name = 'dataflow_cont',
            mounts = [Mount(type='bind',source='home/luna',target='home/jovyan')],
            command = 'python codes/extract.py'
            )

    extract

print('SUCCESS')

```

