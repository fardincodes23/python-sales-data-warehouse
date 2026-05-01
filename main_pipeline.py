import logging
import time
from generate_data import generate_sales_data
from load_data import load_to_database

# 1. Setup Logging: This creates a text file that records everything the pipeline does
logging.basicConfig(
    filename='pipeline_execution.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_etl_pipeline():
    logging.info("=== Starting Daily Sales ETL Pipeline ===")
    start_time = time.time()
    
    try:
        # Step 1: EXTRACT
        print("Starting Extract...")
        logging.info("Step 1: Extracting raw data...")
        df_raw = generate_sales_data()
        df_raw.to_csv('raw_sales_data.csv', index=False)
        logging.info(f"Successfully generated and saved {len(df_raw)} raw records.")
        
        # Step 2 & 3: TRANSFORM & LOAD
        # Because your load_data script already imports and runs the transform_data script,
        # calling this one function handles both the 'T' and the 'L'!
        print("Starting Transform and Load...")
        logging.info("Step 2 & 3: Transforming data and Loading to SQLite database...")
        load_to_database() 
        logging.info("Successfully loaded clean data into the data warehouse.")
        
        # Finish
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        logging.info(f"=== Pipeline Completed Successfully in {duration} seconds ===\n")
        print(f"Pipeline SUCCESS! It took {duration} seconds. Check 'pipeline_execution.log' for details.")
        
    except Exception as e:
        # If ANYTHING fails above, the pipeline stops and logs the exact error
        logging.error(f"PIPELINE FAILED: {e}\n")
        print(f"Pipeline FAILED! Check 'pipeline_execution.log' for details.")

if __name__ == "__main__":
    run_etl_pipeline()