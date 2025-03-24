def read_transaction_file(file_path):
    print("read_transactio_file works")
    ## Reads Transaction File
    ## And outputs array of transaction dictionaries
    ## IMPORTANT: I took out the miscellaneous characters from the code and test file so that it only works with 38 characters

    Transactions = []
    with open(file_path, 'r') as file:
        print("open file works")
        for line_num, line in enumerate(file, 1):
            # Remove newline but preserve other characters
            clean_line = line.rstrip('\n')

            # Validate line length
            if len(clean_line) != 38:
                print(f"ERROR: Fatal error - Line {line_num}: Invalid length ({len(clean_line)} chars)")
                continue

            try:
                # Extract fields with positional validation
                transaction_code = clean_line[0:2] # 2 characters
                account_holder_name = clean_line[3:23]  # 20 characters
                account_holder_number = clean_line[24:29] # 5 characters
                transaction_amount = clean_line[30:38]  # 8 characters

                # Validate transaction code format (2 digits)
                if not transaction_code.isdigit():
                    print(f"ERROR: Fatal error - Line {line_num}: Invalid transaction code format")
                    continue

                ## TODO test if account holder name is properly formated


                # Validate transaction amount format (XXXXX.XX)
                if (len(transaction_amount) != 8 or
                        transaction_amount[5] != '.' or
                        not transaction_amount[:5].isdigit() or
                        not transaction_amount[6:].isdigit()):
                    print(f"ERROR: Fatal error - Line {line_num}: Invalid balance format")
                    continue

                # Validate account holder number format
                if not account_holder_number.isdigit():
                    print(f"ERROR: Fatal error - Line {line_num}: Invalid account number format")
                    continue



                # Convert numerical values
                ## TODO test proper data type



                Transactions.append({
                    'transaction_code': transaction_code ,
                    'name': account_holder_name,
                    'account_number': account_holder_number,
                    'transaction_amount': transaction_amount,
                })

            except Exception as e:
                print(f"ERROR: Fatal error - Line {line_num}: Unexpected error: {str(e)}")
                continue

    return Transactions
