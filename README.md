# Data Pipeline Exercise

## Objective
The goal of this exercise is to design and implement a data pipeline that extracts data from a public API, processes it, and stores it in a relational database. The pipeline should be able to handle data extraction, data transformation, and data storage.

---

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
5. [Running the Pipeline](#running-the-pipeline)
6. [Code Explanation](#code-explanation)
7. [Bonus Features](#bonus-features)
8. [License](#license)

---

## Overview

This project demonstrates how to build a simple data pipeline. The pipeline:

1. **Extracts** data from a public API (weather, cryptocurrency, or COVID-19 data).
2. **Transforms** the data:
   - Handles missing values.
   - Converts timestamps to a standard format.
   - Normalizes numerical values.
3. **Stores** the processed data in a relational database, such as SQLite or PostgreSQL.

The pipeline is designed to be simple yet effective, providing insights into common data engineering tasks like ETL (Extract, Transform, Load).

---

## Project Structure

```bash
data-pipeline/
│
├── data/
│   └── raw_data.json # Sample raw data extracted from the API (optional for testing)
│
├── src/
│   ├── pipeline.py # Main script to run the pipeline (extract, transform, load)
│   ├── api_connector.py # Script to handle API requests and data extraction
│   ├── data_transformer.py # Script to handle data cleaning and transformations
│   └── db_connector.py # Script to handle database connection and storing data
│
├── requirements.txt # Python dependencies
├── schema.sql # SQL script to create the database schema
└── README.md # Project documentation (this file)
```


---

## Prerequisites

To run this project, you'll need:

- Python 3.x installed on your machine.
- A database system (SQLite or PostgreSQL) installed. For SQLite, no setup is needed since it stores data locally in a file.
- The following Python libraries:
  - `requests` (for making HTTP requests to the API)
  - `pandas` (for data manipulation)
  - `sqlalchemy` (for database interaction)
  - `psycopg2` (only if using PostgreSQL)

You can install the dependencies by running:

`pip install -r requirements.txt`
Or using poetry
`poetry install`


---

## Setup Instructions

1. **Database Setup**:
   - For SQLite: The database will be created automatically in the `src/` folder when running the pipeline.
   - For PostgreSQL: Set up a PostgreSQL instance, create a database, and adjust the database connection settings in `db_connector.py` with your credentials.

2. **API Key Setup**:
   - If your chosen API requires an API key, make sure to place the key in the script or store it as an environment variable.

---

## Running the Pipeline

1. **Run the pipeline**:
   - Run the main pipeline script:

     ```bash
     python src/pipeline.py
     ```

   This will:
   - Extract data from the API.
   - Transform the data (cleaning, formatting).
   - Store the data in the configured database.

2. **Check the database**:
   - After running the pipeline, the transformed data should be available in your database under the specified table.

---

## Code Explanation

- **api_connector.py**:
   - Handles the HTTP request to the public API and extracts the data.
   - Handles any rate limits or retries as needed.

- **data_transformer.py**:
   - Cleans the extracted data:
     - Handles missing values (e.g., by replacing with a default value or removing rows).
     - Converts timestamps to a uniform format (e.g., ISO 8601).
     - Normalizes numeric fields.

- **db_connector.py**:
   - Connects to the relational database and creates tables as per the schema (defined in `schema.sql`).
   - Inserts the transformed data into the database.

- **pipeline.py**:
   - The main script that orchestrates the execution of the entire pipeline, from extraction to storage.

---

## Bonus Features

1. **Error Handling**: The pipeline includes error handling for API failures, database connection issues, and invalid data formats.
2. **Scheduling**: For regular execution, you can use `cron` jobs or task schedulers to run the pipeline periodically.
3. **Logging**: Detailed logging has been implemented using the `logging` library to track the flow of data through the pipeline.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
