#!/bin/bash

# Output file
OUTFILE="lengths1run.txt"

# Clear any previous results
> "$OUTFILE"

# Run the Python program 100 times
for i in {1..100}
do
    # Run the solver, feed it input.txt, take only the first line (the length)
    LENGTH=$(python3 cs412_tsp_approx_v2.5.py < 108_11_input.txt | head -n 1)
    echo "$LENGTH" >> "$OUTFILE"
done
