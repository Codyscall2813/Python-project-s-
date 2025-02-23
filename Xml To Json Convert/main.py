import json
import xmltodict
import os

def xml_to_json(xml_file_path, json_file_path):
    try:
        # Check if the input XML file exists
        if not os.path.isfile(xml_file_path):
            print(f"Input XML file {xml_file_path} does not exist.")
            return
        
        print(f"Reading XML data from {xml_file_path}...")
        with open(xml_file_path, 'r') as xml_file:
            xml_content = xml_file.read()
        
        print("Parsing XML data...")
        parsed_data = xmltodict.parse(xml_content)

        print("Converting XML data to JSON format...")
        json_data = json.dumps(parsed_data, indent=4)

        # Write JSON data to the output file
        print(f"Writing JSON data to {json_file_path}...")
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)
        
        print("Conversion completed successfully.")

    except Exception as ex:
        print(f"Error: {str(ex)}")

if __name__ == '__main__':
    input_xml_path = 'Collection/Xml to JSON Convert/input.xml'
    output_json_path = 'Collection/Xml to JSON Convert/output.json'
    xml_to_json(input_xml_path, output_json_path)
