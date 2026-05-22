# main.py
import config
from data_api import fetch_world_bank_data
from functions import preprocess_data
import logging
import os

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO, format=config.LOGGING_FORMAT)
    logging.info("--- Starting Data Extraction Pipeline ---")
    
    # 1. Fetch Data
    raw_data = fetch_world_bank_data(
        countries=config.TARGET_COUNTRIES, 
        indicators=config.INDICATORS,
        start_year=config.START_YEAR,
        end_year=config.END_YEAR
    )
    
    # 2. Preprocess Data
    clean_panel_data = preprocess_data(raw_data)
    
    if clean_panel_data.empty:
        logging.error("Pipeline terminated due to empty data.")
        return

    # 3. Export to CSV for Jupyter Notebook
    output_filename = 'world_bank_panel_data.csv'
    clean_panel_data.to_csv(output_filename)
    logging.info(f"Success! Data successfully saved to '{output_filename}'")
    logging.info("You can now open your Jupyter Notebook and load this CSV.")

if __name__ == "__main__":
    main()