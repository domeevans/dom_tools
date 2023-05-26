import pandas as pd
import re

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean column names in a DataFrame by converting camel case to snake case,
    replacing punctuation with underscores, and trimming leading/trailing underscores.

    Args:
        df (pd.DataFrame): The DataFrame with column names to be cleaned.

    Returns:
        pd.DataFrame: The DataFrame with cleaned column names.

    Examples:
        df = pd.DataFrame(columns=['thisIsCamelCase', 'another_column', 'some-column'], data=[1, 2, 3])
        clean_column_names(df)
           this_is_camel_case  another_column  some_column
        0                   1               2            3
    """
    # Convert camel case to snake case, replace punctuation with underscores, and trim underscores
    snake_case = lambda name: re.sub(r'[\W_]+', '_', re.sub(r'(?<!^)(?=[A-Z])', '_', name)).strip('_').lower()

    # Apply snake_case function to all column names
    df.columns = [snake_case(name) for name in df.columns]

    return df
