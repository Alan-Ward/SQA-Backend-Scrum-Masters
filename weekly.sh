#!/bin/bash

# Path config
TRANSACTION_DIR=./transactions
BACKEND_MASTER=./backend/Master_Bank_Accounts_File
BACKEND_CURRENT=./backend/New_Current_Bank_Accounts_File

# Loop through each day folder in order
for day_folder in $TRANSACTION_DIR/day{1..7}; do
    echo "============================="
    echo "Processing ${day_folder}"
    echo "============================="

    # Replace input.txt pointer in daily.sh with day-specific file before each run
    sed -i "s|input_file=.*|input_file=\"${day_folder}/input.txt\"|" ./daily.sh
    sed -i "s|output_file=.*|output_file=\"${day_folder}/transactions.txt\"|" ./daily.sh

    # If not day1, use output from previous day as new master input
    if [[ "$day_folder" != "$TRANSACTION_DIR/day1" ]]; then
        cp $BACKEND_CURRENT $BACKEND_MASTER
    fi

    bash ./daily.sh
done
