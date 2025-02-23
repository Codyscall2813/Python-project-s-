import json
import os

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Check if the input file exists
        if not os.path.isfile(json_file_path):
            print(f"Input file {json_file_path} does not exist.")
            return
        
        print(f"Reading JSON data from {json_file_path}...")
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        
        if not data:
            print("No data found in JSON file.")
            return

        print("Converting JSON data to CSV format...")
        # Create CSV header from the first item's keys
        headers = ','.join(data[0].keys())
        rows = [headers]
        
        # Convert each JSON object to a CSV row
        for obj in data:
            row = ','.join(str(obj.get(field, '')) for field in data[0].keys())
            rows.append(row)

        # Write CSV data to the output file
        print(f"Writing CSV data to {csv_file_path}...")
        with open(csv_file_path, 'w') as f:
            f.write('\n'.join(rows))
        
        print("Conversion completed successfully.")

    except Exception as ex:
        print(f"Error: {str(ex)}")

if __name__ == '__main__':
    input_json = 'Collection/Json to CSV Convert/input.json'
    output_csv = 'Collection/Json to CSV Convert/output.csv'
    json_to_csv(input_json, output_csv)
