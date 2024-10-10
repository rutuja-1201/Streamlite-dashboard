
import pandas as pd

def load_data(file_path):
    """Load dataset and return a cleaned dataframe."""
    df = pd.read_csv(file_path)
  
    return df
