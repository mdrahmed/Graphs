import os
import subprocess

# Define the list of seq_len and topk values
seq_len_values = [512, 1024]
topk_values = [1000, 2000, 5000, 7000, 10000]

# Create a directory to store the output files
output_dir = "output_files"
os.makedirs(output_dir, exist_ok=True)

# Iterate through the combinations and run the command
for seq_len in seq_len_values:
    for topk in topk_values:
        # Define the output directory for this combination
        output_subdir = f"output_seq_{seq_len}_topk_{topk}"
        os.makedirs(os.path.join(output_dir, output_subdir), exist_ok=True)

        # Run the command with the current seq_len and topk values
        cmd = f"python3 ./find_and_remove.py --fnames hbwall3-vgrall3 --split_mode overlapping --seq_len {seq_len} --topk {topk} --fname_to_remove hbwall3 --common_threshold 0.1"
        subprocess.run(cmd, shell=True, cwd=os.path.join(output_dir, output_subdir), check=True)

