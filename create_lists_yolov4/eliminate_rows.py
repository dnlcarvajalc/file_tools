import pandas as pd


df = pd.read_csv('results.txt', header=None, names=['Column1'])

# Define the suffix you want to check for
suffix = '.txt'

# Create a Boolean mask to filter rows
mask = df['Column1'].str.endswith(suffix)

# Apply the mask to the DataFrame
filtered_df = df[~mask]

# Display the filtered DataFrame
print(filtered_df)

filtered_df.to_csv('filtered_data.txt', header=False, index=False)