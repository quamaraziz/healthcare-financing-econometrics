# data_api.py
import wbgapi as wb
import pandas as pd
import logging
from typing import List, Dict

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_world_bank_data(countries: List[str], indicators: Dict[str, str], start_year: int, end_year: int) -> pd.DataFrame:
    """
    Fetches panel data from the World Bank API robustly.
    """
    logging.info("Starting data fetch from World Bank API...")
    
    try:
        indicator_codes = list(indicators.keys())
        time_range = range(start_year, end_year + 1)
        
        # Fetch data WITHOUT labels=True or numericTimeKeys=True to prevent wbgapi crashes
        df = wb.data.DataFrame(
            indicator_codes, 
            economy=countries, 
            time=time_range
        )
        
        # Reset index (this turns the 'economy' and 'series' indices into columns)
        df = df.reset_index()
        
        # Melt the years into rows. The year columns will look like 'YR2000', 'YR2001', etc.
        df_melted = df.melt(id_vars=['economy', 'series'], var_name='year', value_name='value')
        
        # Manually strip 'YR' from the year column and convert to integer
        df_melted['year'] = df_melted['year'].str.replace('YR', '').astype(int)
        
        # Pivot so each indicator gets its own column
        df_panel = df_melted.pivot_table(index=['economy', 'year'], columns='series', values='value').reset_index()
        
        # Remove the 'series' name from the columns index for cleaner output
        df_panel.columns.name = None
        
        # Rename columns using our config mapping
        df_panel.rename(columns=indicators, inplace=True)
        df_panel.rename(columns={'economy': 'country'}, inplace=True)
        
        logging.info(f"Successfully fetched data: {df_panel.shape[0]} rows.")
        return df_panel

    except Exception as e:
        logging.error(f"Failed to fetch data from API: {e}")
        return pd.DataFrame() # Return empty dataframe on failure