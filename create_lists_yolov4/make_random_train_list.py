import random
import pandas as pd

# List of all text elements
df = pd.read_csv('filtered_data.txt', header=None, names=['Column1'])

# Set the random seed for reproducibility
df_randomized = df.sample(frac=1, random_state=42)

# Define the split ratio for training and validation
train_ratio = 0.9  # 90% for training, 10% for validation

# Calculate the split index
split_index = int(len(df) * train_ratio)

# Split the list into training and validation lists
train_list = 'data/ob/' + df_randomized[:split_index]
valid_list = 'data/ob/' + df_randomized[split_index:]

# Print the training and validation lists
print("Training list:", train_list)
train_list.to_csv('train.txt', header=False, index=False)
print("Validation list:", valid_list)
valid_list.to_csv('valid.txt', header=False, index=False)