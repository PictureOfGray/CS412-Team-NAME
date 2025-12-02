#!/bin/bash

# Output file
OUTFILE="exact_time_output.txt"

# Clear any previous results
> "$OUTFILE"

# Run the Python program 100 times
for i in {1..100}
do
    # Run the solver, feed it input.txt, take only the first line (the length)
    LENGTH=$(python3 ../exact_solution/cs412_tsp_exact.py test < in.txt | head -n 1)
    echo "$LENGTH" >> "$OUTFILE"
done
