# config.py

# Timeframe for the analysis
START_YEAR = 2000
END_YEAR = 2024

# Fetching global data to eliminate selection bias
TARGET_COUNTRIES = 'all' 

# The Finalized Econometric Explanatory Variables
INDICATORS = {
    # Target Variable
    'SH.XPD.OOPC.CH.ZS': 'oop_spending',       
    
    # Core Economic Drivers
    'NY.GDP.PCAP.CD': 'gdp_per_capita',        
    'SH.XPD.GHED.GD.ZS': 'gov_health_exp',     
    'SH.UHC.SRVS.CV.XD': 'insurance_coverage', # UHC Index proxy
    
    # Demographic & Macro Controls
    'SP.POP.65UP.TO.ZS': 'pop_65_plus',        
    'FP.CPI.TOTL.ZG': 'inflation_rate'
}

# Logging configuration
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Non-reporting entities, macro-regions, and aggregates to drop at the source
ENTITIES_TO_DROP = [
    'AND', 'ARB', 'ARG', 'ASM', 'BMU', 'CEB', 'CHI', 'CSS', 'CUB', 'CYM', 
    'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 'EMU', 'ERI', 'EUU', 'FCS', 'FRO', 
    'GIB', 'GRL', 'GUM', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA', 'IDB', 'IDX', 
    'IMN', 'LAC', 'LCN', 'LDC', 'LIC', 'LIE', 'LMC', 'LMY', 'LTE', 'MAF', 
    'MCO', 'MEA', 'MHL', 'MIC', 'MNA', 'MNP', 'NAC', 'NCL', 'NRU', 'OED', 
    'OSS', 'PRE', 'PRI', 'PRK', 'PSS', 'PST', 'PYF', 'SAS', 'SOM', 'SSA', 
    'SSF', 'SST', 'SXM', 'TCA', 'TEA', 'TEC', 'TKM', 'TLA', 'TMN', 'TSA', 
    'TSS', 'TUV', 'UMC', 'VEN', 'VGB', 'VIR', 'WLD'
]