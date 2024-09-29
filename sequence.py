### README
### odd number row -> mutant, even number row -> control (non-mutated)
### each sequence contains 41 nucleotides. For the ones containing the mutant, the mutant is in the center
### I used the filtered csv file (with the first row removed)

import genome_kit as gk
import csv
import re

with open('chr_filtered_results.csv', mode='r') as input:
    with open('output.csv', 'w', newline='') as output:
        csv_reader = csv.reader(input)
        line_count = 0
        for row in csv_reader:
            genome = gk.Genome("hg38.p12")

            SNP_val = str((row[0]))
            
            # set interval
            #chrom = re.match(r"(chr\d+)", SNP_val).group(1)
            chrom = re.match(r"(chr[\dXY]+)", SNP_val).group(1)
            specifier = int(re.search(r"chr[\dXY]+:(\d+):", SNP_val).group(1))
            #print(f"Chrom: {chrom}")
            #print(f"Specifier: {specifier}")
            i = gk.Interval(chrom, '+', specifier - 21, specifier + 20, genome) # interval containing this varient

            # creating variant 
            variant = gk.Variant.from_string(SNP_val, genome) #creating a genome kit varient object
            #print(variant)
            #print(genome)
            var_genome = gk.VariantGenome(genome, variant) # creating a genome with the above varient

            genome1 = str(var_genome)
            
            # write to csv
            output.write(var_genome.dna(i))
            output.write("\n")
            output.write(genome.dna(i))
            output.write("\n")



