# Data Flow

![https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/workflow.svg](https://github.com/AllanMogley/1-data_flow/blob/main/1-assets/workflow.svg)

This system focuses on the development of a data pipeline to extract, transform, and load **(ETL)** data from a hosted source into our inhouse database. The ETL process will involve extracting relevant data from the source database using Python APIs, transforming the data to align with the database schema and loading the transformed data into our target infrastructure.

The data pipeline will be designed to be scalable, efficient, and reliable, ensuring timely and accurate data integration. Additionally, we will implement error handling and logging mechanisms to monitor the pipeline's performance and troubleshoot any issues.

### Tools and Skills:

1. Docker Images and Containers
2. Apache Airflow for data systems orchestration
3. Python scripting
4. basic Linux knowledge

### This is how we’ll do it:

1. Configure our environment and install our libraries. A docker container will host all out codes.
2. Code the algorithm to extract the data from the hosted database and loads into our landing zone
3. Write algorithms to transform this data and load to our staging zone
4. Write a schema that matches our inhouse database
5. Load the data onto our database
