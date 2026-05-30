# Code to generate the parquet file from the dataset provided
# Team members - 1.Nitin Mereddy 
# 2. Riswana Palliyaliyil

import os                  # For handling file paths
from PIL import Image      # For image processing
import pandas as pd        # For data handling
import numpy as np         # For working with arrays

dataset_path = "C:\\Advanced Project dataset\\TB_Chest_Radiography_Database"
data = []                 
image_size = (224, 224)    

for label in os.listdir(dataset_path):  
    class_path = os.path.join(dataset_path, label)  
    
    # Check if the path is actually a folder
    if os.path.isdir(class_path):
        
        # Loop through each image in the class folder
        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)  
            
            try:
                # Open the image, resize it, and convert it to a numpy array
                img = Image.open(image_path)          # Open the image
                img = img.resize(image_size)          # Resize the image to the defined size
                img_array = np.array(img)             # Convert the image to an array
                img_array = img_array.flatten()       # Flatten the array to make it 1D
                
                # Add the image data and label to the data list
                data.append([img_array, label])       
            
            except Exception as e:

                print("Error processing", image_path, ":", e)

# Create a DataFrame from the data list, with columns for image data and label
df = pd.DataFrame(data, columns=["image_data", "label"])

# Save the DataFrame to a .parquet file format
df.to_parquet('chest_xray_data.parquet')
print("Parquet file created with initial data.")

# Load the saved .parquet file to check if it saved correctly
df = pd.read_parquet('chest_xray_data.parquet')

