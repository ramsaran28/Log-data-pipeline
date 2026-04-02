# Log Data Pipeline with FastAPI

## Overview

This project is a simple backend data pipeline that processes system log data and exposes it through a REST API. It simulates how real-world applications handle logs for monitoring and analysis.

The pipeline reads raw log data, cleans and structures it, stores the processed output, and allows users to query it through an API.

## Features

* Ingests raw log data from CSV
* Processes and cleans log entries
* Stores structured output
* Exposes logs through a FastAPI endpoint
* Supports filtering logs by level (INFO, ERROR, WARNING)

## Tech Stack

* Python
* FastAPI
* Pandas

## Project Structure

log-data-pipeline/

data/

* logs.csv
* processed_logs.csv

pipeline/

* ingest.py
* transform.py
* store.py

api/

* main.py

run_pipeline.py
README.md

## How It Works

1. The pipeline reads raw logs from logs.csv
2. Data is cleaned and structured
3. Processed data is saved as processed_logs.csv
4. FastAPI serves this data through an endpoint

## Running the Project

1. Install dependencies
   python3 -m pip install pandas fastapi uvicorn

2. Run the pipeline
   python3 run_pipeline.py

3. Start the API server
   uvicorn api.main:app --reload

## API Usage

Get all logs
http://127.0.0.1:8000/logs

Filter logs by level
http://127.0.0.1:8000/logs?level=ERROR
http://127.0.0.1:8000/logs?level=INFO

## Example Output

[
{
"timestamp": "2026-04-01",
"level": "ERROR",
"message": "Database connection failed"
}
]

## What I Learned

Through this project, I learned how to:

* Build a simple ETL (Extract, Transform, Load) pipeline
* Work with structured data using Pandas
* Create REST APIs using FastAPI
* Connect backend processing with API endpoints

## Future Improvements

* Add database storage (PostgreSQL / MongoDB)
* Add authentication to API
* Deploy on cloud (AWS / GCP)
* Build a frontend dashboard for visualization

## Author

Ram Saran
