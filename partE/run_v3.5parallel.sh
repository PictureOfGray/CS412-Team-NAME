#!/bin/bash

# Output file
OUTFILE="v3.5parallel_length_output.txt"

# Clear any previous results
> "$OUTFILE"

# Run the Python program 100 times
for i in {1..100}
do
    # Run the solver, feed it input.txt, take only the first line (the length)
    LENGTH=$(python3 cs412_tsp_approx_v3.5_parallelized.py < in.txt | head -n 1)
    echo "$LENGTH" >> "$OUTFILE"
done
