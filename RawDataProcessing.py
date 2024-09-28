import pandas as pd

# Define the paths for your input text files
file1_path = r'Extracurriculars\TorontoBioinformatics2024\Meta_COGRES_females_p-valueonly.txt'  # First text file path
file2_path = r'Extracurriculars\TorontoBioinformatics2024\Meta_COGRES_NC_females_p-valueonly.txt'  # Second text file path

# Read the text files into pandas DataFrames
df1 = pd.read_csv(file1_path, sep=' ', header=0)  # Adjust sep if necessary
df2 = pd.read_csv(file2_path, sep=' ', header=0)  # Adjust sep if necessary

# Filter the DataFrames for P values <= 0.05 and create a copy to avoid warnings
filtered_df1 = df1[df1['P'] <= 0.05].copy()
filtered_df2 = df2[df2['P'] <= 0.05].copy()

# Add a new column for "Alzheimer Disease" with a value of 1 for entries in df1 and 0 for df2
filtered_df1.loc[:, 'Alzheimer Disease'] = 1
filtered_df2.loc[:, 'Alzheimer Disease'] = 0

# Combine the DataFrames
combined_df = pd.concat([filtered_df1, filtered_df2], ignore_index=True)

# Count unique SNP entries
unique_snps = combined_df['SNP'].nunique()

# Save the filtered DataFrame to a CSV file
output_csv_path = r'Extracurriculars\TorontoBioinformatics2024\filtered_results.csv'  # Output CSV file path
combined_df.to_csv(output_csv_path, index=False)

# Print the number of unique SNPs
print(f"Number of unique SNP entries: {unique_snps}")
print(f"Filtered results saved to: {output_csv_path}")
