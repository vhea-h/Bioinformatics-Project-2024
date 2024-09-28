import pandas as pd

# Specify the input CSV file path
input_csv_path = r'Extracurriculars\TorontoBioinformatics2024\chr_filtered_results.csv'  # Replace with your actual file path

# Specify the output VCF file path
output_vcf_path = r'Extracurriculars\TorontoBioinformatics2024\chr_filtered_results_vcf.vcf'  # Replace with your desired output file path

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_path)

# Prepare to write to the VCF file
with open(output_vcf_path, 'w') as vcf_file:

    # Write the VCF header
    vcf_file.write("##fileformat=VCFv4.2\n")  # Specify VCF version
    vcf_file.write("SNP\tEffectAllele\tAlternateAllele\tP\tAlzheimer Disease\tVariantInfo\n")  # Column headers

    # Convert each row of the DataFrame to VCF format
    for _, row in df.iterrows():
        # Extract necessary fields
        SNP = row['SNP']  
        EffectAllele = row['EffectAllele'] 
        AlternateAllele = row['AlternateAllele']  
        P = row['P']  
        VariantInfo = row['VariantInfo'] 
        Alzheimer_Disease = row['Alzheimer Disease']  
        
        # Create ID based on VariantInfo or use '.' if not applicable
        id_ = row['VariantInfo'] if row['VariantInfo'] else '.'

        # Write the data line to the VCF file
        vcf_line = f"{SNP}\t{EffectAllele}\t{AlternateAllele}\t{P}\t{Alzheimer_Disease}\t{VariantInfo}"
        vcf_file.write(vcf_line + '\n')

print(f"VCF file saved to: {output_vcf_path}")
