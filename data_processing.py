import sys
import csv

def read_input_file(file_name):
    """Reads data from the input file (CSV format)."""
    try:
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader)
            # Read data values (assuming numerical data in the second column)
            for row in reader:
                try:
                    data.append(float(row[1]))  # Assuming the second column holds the numerical values
                except ValueError:
                    print(f"Error: Invalid data found in row: {row}")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        sys.exit(1)

def perform_calculations(data):
    """Performs two calculations on the input data."""
    # Calculation 1: Sum of all the numbers
    total_sum = sum(data)
    
    # Calculation 2: Average of the numbers
    average = total_sum / len(data) if data else 0
    
    return total_sum, average

def write_output_file(output_file, total_sum, average):
    """Writes the results to an output file."""
    try:
        with open(output_file, 'w') as file:
            file.write(f"Total Sum: {total_sum}\n")
            file.write(f"Average: {average}\n")
    except IOError:
        print(f"Error: Unable to write to the file {output_file}.")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python data_processing.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read input data
    data = read_input_file(input_file)

    # Perform calculations
    total_sum, average = perform_calculations(data)

    # Write output data
    write_output_file(output_file, total_sum, average)
    print(f"Results have been written to {output_file}")

if __name__ == '__main__':
    main()
