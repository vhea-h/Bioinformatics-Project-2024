import numpy as np
import pandas as pd
import torch
import os

import grelu.resources

model = grelu.resources.load_model(
    project="borzoi",
    model_name="human_fold0",
)

model.data_params.keys()
for key in model.data_params.keys():
    if key !="tasks":
        print(key, model.data_params[key])
        
tasks = pd.DataFrame(model.data_params['tasks'])
tasks.head(3)

input_len = model.data_params["train_seq_len"]
chrom = "chr1"
input_start = 69993520
input_end = input_start + input_len

input_intervals = pd.DataFrame({
    'chrom':[chrom], 'start':[input_start], 'end':[input_end], "strand":["+"],
})

input_intervals

import grelu.sequence.format

input_seqs = grelu.sequence.format.convert_input_type(
    input_intervals,
    output_type="strings",
    genome="hg38"
)
input_seq = input_seqs[0]

len(input_seq)

input_seq[:10]

cage_brain_tasks = tasks[(tasks.assay=="CAGE") & (tasks["sample"].str.contains("brain"))].head(2)
rna_brain_tasks = tasks[(tasks.assay=="RNA") & (tasks["sample"].str.contains("brain"))].head(2)

tasks_to_plot = cage_brain_tasks.index.tolist() + rna_brain_tasks.index.tolist()
task_names = tasks.description[tasks_to_plot].tolist() # Description of these tracks from the `tasks` dataframe

print(tasks_to_plot)
print(task_names)