import pandas as pd

# Specify the path to your input CSV file
input_file_path = r'Extracurriculars/TorontoBioinformatics2024/filtered_results.csv'  # Replace with your actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file_path, sep=',', header=0)  # Adjust sep if necessary

# Filter the DataFrame for entries where the 'SNP' column starts with 'chr'
filtered_df = df[df['SNP'].str.startswith('chr')]

# Specify the path for the output CSV file
output_file_path = r'Extracurriculars/TorontoBioinformatics2024/chr_filtered_results.csv'  # Replace with your desired output file path

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file_path, index=False)

print(f"Filtered results saved to: {output_file_path}")
