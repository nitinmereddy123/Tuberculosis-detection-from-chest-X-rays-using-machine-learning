#Code to split the dataset into Training, Validation and Testing subsets
# #Team Members
#Nitin Mereddy
#Riswana Palliyaliyil
import os
import shutil
from sklearn.model_selection import train_test_split

def split_images_simple(input_folder, output_train, output_val, output_test, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    """
    Splits images into training, validation, and test sets.

    Args:
        input_folder (str): Folder with class subfolders containing images.
        output_train (str): Folder to save training images.
        output_val (str): Folder to save validation images.
        output_test (str): Folder to save test images.
        train_ratio (float): Fraction of data for training (default: 0.8).
        val_ratio (float): Fraction of data for validation (default: 0.1).
        test_ratio (float): Fraction of data for testing (default: 0.1).
    """
    # Checks whether the sum of ratios is 1 or not
    if train_ratio + val_ratio + test_ratio != 1.0:
        raise ValueError("Train, validation, and test ratios must add up to 1!")

    for folder in [output_train, output_val, output_test]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    for category in os.listdir(input_folder):
        class_folder = os.path.join(input_folder, category)

        if not os.path.isdir(class_folder):
            continue

        # Get all image file paths in this class folder
        image_files = [os.path.join(class_folder, file) for file in os.listdir(class_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # Splits the images into train_val and test sets
        train_val_split, test_split = train_test_split(image_files, test_size=test_ratio, random_state=42)

        # Seperates the train_val into training and validation sets 
        train_split, val_split = train_test_split(train_val_split, test_size=val_ratio / (train_ratio + val_ratio), random_state=42)

        # Saves the images into the folders
        for output_folder, split in zip([output_train, output_val, output_test], [train_split, val_split, test_split]):
            class_output_folder = os.path.join(output_folder, category)
            if not os.path.exists(class_output_folder):
                os.makedirs(class_output_folder)
            for image in split:
                shutil.copy(image, os.path.join(class_output_folder, os.path.basename(image)))
#confirms the splits
    print("Image splitting completed!")
    print(f"Training images saved in: {output_train}")
    print(f"Validation images saved in: {output_val}")
    print(f"Test images saved in: {output_test}")

# Define the paths of source and output folders
source_folder = r"C:\Advanced Project dataset\TB_Chest_Radiography_Database"
train_output = r"\\wsl.localhost\Ubuntu\home\nitin123\DF\df-analyze\X-Vision\X-vision-helper\Train"
val_output = r"\\wsl.localhost\Ubuntu\home\nitin123\DF\df-analyze\X-Vision\X-vision-helper\Val"
test_output = r"\\wsl.localhost\Ubuntu\home\nitin123\DF\df-analyze\X-Vision\X-vision-helper\Test"

# Calls the function to split the images
split_images_simple(source_folder, train_output, val_output, test_output)
