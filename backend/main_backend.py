from src.BankBackend import BackEnd
import os

def convert_long_to_short(account_str):
    """Converts a bank account string from long to short format by removing the last 2 fields."""
    parts = account_str.strip().split()
    if len(parts) >= 4:  # Ensure valid format (e.g., "12345 Andrew A 00300.00 0001 NP")
        return ' '.join(parts[:-2])  # Remove last 2 fields
    return account_str  # Return unchanged if invalid

def process_files():
    # Define file paths
    input_path = os.path.join(os.path.dirname(__file__), '..', 'Master_Bank_Accounts_File.txt')
    output_path = os.path.join(os.path.dirname(__file__), '..', '..', 'bank_account.txt')

    # Read input file (long format)
    with open(input_path, 'r') as f_in:
        lines = f_in.readlines()

    # Convert each line to short format
    short_lines = [convert_long_to_short(line) + '\n' for line in lines]

    # Write output file (short format)
    with open(output_path, 'w') as f_out:
        f_out.writelines(short_lines)
def main():
    backend = BackEnd()
    try:
        backend.run()
        process_files()
    except EOFError:
        pass
if __name__ == "__main__":
    main()