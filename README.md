# 🚀 Automated Python ETL Pipeline: Synthetic Sales Data Warehouse

## 📌 Project Overview
This project is an end-to-end, fully automated Extract, Transform, and Load (ETL) pipeline built entirely in Python. It generates synthetic e-commerce sales data, cleans and processes the records using Pandas, and loads the structured results into a relational SQLite Data Warehouse. 

The pipeline is orchestrated via a master control script with built-in logging, error handling, and modular execution. Drawing from enterprise data migration strategies, this architecture mirrors the robustness of traditional workload automation platforms (like Universal Automation Center) and integration services (like SSIS), but implements them using a modern, code-first Python stack.

This project was specifically designed to demonstrate practical application of **Microsoft Azure Data Fundamentals (DP-900)** concepts in a local environment.

## ☁️ Cloud Architecture Mapping (Azure DP-900)
While this pipeline runs locally, it is architected to perfectly simulate a modern Azure cloud data solution. Here is how the local components map to enterprise Azure services:

| Local Implementation | ETL Phase | Azure Cloud Equivalent | Description |
| :--- | :--- | :--- | :--- |
| `generate_data.py` (CSV Output) | **Extract** | **Azure Data Lake Storage Gen2** | Landing zone for raw, semi-structured data ingestion. |
| `transform_data.py` (Pandas) | **Transform** | **Azure Synapse Analytics / Databricks** | Vector-based data cleaning, type casting, and business logic application. |
| `load_data.py` (SQLite) | **Load** | **Azure SQL Database** | Relational storage utilizing strict schema definitions for analytical querying. |
| `main_pipeline.py` | **Orchestrate**| **Azure Data Factory (ADF)** | Pipeline orchestration, dependency management, and execution logging. |

## ⚙️ Pipeline Execution Flow

1. **Extract (`generate_data.py`):** Uses the `Faker` library to generate randomized transactional sales records (simulating live API ingestion) and lands them in a raw CSV file.
2. **Transform (`transform_data.py`):** Ingests the raw data into a Pandas DataFrame. It removes duplicates, drops null values, standardizes geographic strings, casts dates to proper `datetime` objects, and dynamically calculates a new `total_sale` metric.
3. **Load (`load_data.py`):** Connects to a local SQLite database, defines a relational schema (`fact_sales`), and seamlessly loads the transformed Pandas DataFrame into the data warehouse for downstream analytics.
4. **Orchestrate (`main_pipeline.py`):** The master control flow script. It executes the ETL phases sequentially, tracks execution time, and records all activities (including fatal errors) to a `pipeline_execution.log` file for auditing.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.x
* **Data Processing:** `pandas`
* **Database:** `sqlite3` (Built-in)
* **Data Generation:** `Faker`
* **Core Libraries:** `logging`, `time`, `random`
