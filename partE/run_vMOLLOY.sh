#!/bin/bash

# Output file
OUTFILE="molloy_output.txt"

# Clear any previous results
> "$OUTFILE"

# Run the Python program 100 times
# Run the solver, feed it input.txt, take only the first line (the length)
LENGTH=$(python3 cs412_tsp_approx_v_MOLLOY.py < in.txt | head -n 1)
echo "$LENGTH" >> "$OUTFILE"
