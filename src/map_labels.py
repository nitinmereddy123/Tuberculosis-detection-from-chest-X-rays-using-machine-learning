#code to map the labels for normal and tuberculosis images
#Team members 1. Nitin Mereddy
# 2. Riswana Palliyaliyil
import pandas as pd               
from PIL import Image             
import numpy as np                

# Path to the .parquet file that we want to load
file_path = "C:\\Users\\nitin\\Downloads\\chest_xray_data.parquet"

# Load the data from the .parquet file into a DataFrame
df = pd.read_parquet(file_path)   # Reads the file and stores it in a DataFrame called 'df'

print("Columns in the DataFrame:", df.columns)

if 'label' in df.columns:
    # Create a dictionary to map label names to integer values
    label_mapping = {
        "Normal": 0,             # Map 'Normal' to 0
        "Tuberculosis": 1        # Map 'Tuberculosis' to 1
    }
    
    
    df['label'] = df['label'].map(label_mapping)
    
    # Define the path to save the modified DataFrame as a new .parquet file
    modified_file_path = "C:\\Users\\nitin\\Downloads\\chest_xray_data_parquet.parquet"
    
    df.to_parquet(modified_file_path)
    
    print("Successfully converted label data to integer values and saved the modified file.")
else:

    print("Column 'label' not found in the DataFrame.")
