import pandas as pd
import re

def clean_column_names(df):
    # Remove punctuation and convert to snake case, replacing parentheses with underscores
    clean_names = lambda name: re.sub(r'[^\w\s]', '', name).lower().replace(' ', '_').replace('(', '_').replace(')', '_')
    
    # Apply clean_names function to all column names
    df.columns = [clean_names(name) for name in df.columns]
    
    return df