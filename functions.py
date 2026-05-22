# functions.py
import pandas as pd
import numpy as np
import logging
import config

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans data, drops non-sovereign entities, and creates log transformations."""
    if df.empty:
        logging.warning("Dataframe is empty. Skipping preprocessing.")
        return df
        
    df_clean = df.copy() 
    
    # 1. THE FILTER: Drop the non-reporting entities and aggregates at the source
    initial_rows = len(df_clean)
    
    # Assuming 'country' is a column right now (before we set the index)
    if 'country' in df_clean.columns:
        df_clean = df_clean[~df_clean['country'].isin(config.ENTITIES_TO_DROP)]
        logging.info(f"Dropped {initial_rows - len(df_clean)} rows belonging to non-reporting entities.")
    
    # 2. Create log transformations safely
    if 'gdp_per_capita' in df_clean.columns:
        df_clean['log_gdp_per_capita'] = np.log(df_clean['gdp_per_capita'] + 1)
    
    # 3. Set panel index
    df_clean = df_clean.set_index(['country', 'year'])
    logging.info(f"Data preprocessed. Total valid rows remaining: {df_clean.shape[0]}")
    
    return df_clean