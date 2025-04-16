#!/bin/bash

# Set directories
FRONTEND_SCRIPT=./frontend/main_frontend.py
BACKEND_SCRIPT=./backend/main_backend.py
TRANSACTION_DIR=./transactions
MERGED_FILE=./backend/Merged_Bank_Account_Transaction_File

# Clean up old merged file
rm -f $MERGED_FILE

# Loop over day folders
for day_dir in $TRANSACTION_DIR/day*; do
    echo "Processing sessions in $day_dir"
    
    # Loop over all session*_input.txt files
    for session_file in "$day_dir"/session*_input.txt; do
        [ -e "$session_file" ] || continue  # skip if no matching file
        session_name=$(basename "$session_file" .txt)
        output_file="./transactions/day7/transactions.txt"
        
        echo "Running session file: $session_file"
        python3 $FRONTEND_SCRIPT < "$session_file"
        
        # Move transaction output to appropriately named file
        mv transaction.txt "$output_file"
        
        # Append to merged file
        cat "$output_file" >> "$MERGED_FILE"
    done
done

# Run backend
echo "Processing with backend..."
python3 $BACKEND_SCRIPT
