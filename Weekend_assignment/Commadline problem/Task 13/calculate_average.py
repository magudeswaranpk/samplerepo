'''13. Implement a Python script that takes a CSV file and two column names as command-line arguments. The script should calculate the average of values in one column and store the result in another column in the same file.'''
import sys
import csv

def calculate_average(input_file, output_file, column_to_average, new_column_name):
    try:
        with open(input_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Calculate the average of values in the specified column
        total = 0
        count = 0
        for row in data:
            try:
                value = float(row[column_to_average])
                total += value
                count += 1
            except ValueError:
                # Handle invalid values gracefully (e.g., non-numeric values)
                pass

        if count > 0:
            average = total / count
        else:
            average = 0

        # Add the new column with the calculated average to the data
        for row in data:
            row[new_column_name] = average

        # Write the updated data back to the output file
        with open(output_file, 'w', newline='') as csv_output_file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Average of '{column_to_average}' column calculated and stored in '{new_column_name}' column.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python calculate_average.py <input_file> <output_file> <column_to_average> <new_column_name>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        column_to_average = sys.argv[3]
        new_column_name = sys.argv[4]
        calculate_average(input_file, output_file, column_to_average, new_column_name)
