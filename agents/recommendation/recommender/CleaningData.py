import json


# Custom parsing function to handle the irregular structure of the CSV file
def parse_custom_csv(file_path):
    data = []
    current_record = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:  # This will ignore lines that are empty when whitespace is stripped
                current_record += ' ' + stripped_line  # Concatenate parts of the same record
            else:
                if current_record:  # If there's a current record built up, it's complete and can be added to data
                    data.append(current_record.strip())
                    current_record = ''  # Reset the current record for the next block of text
        if current_record:  # Make sure to add the last record if the file doesn't end with a newline
            data.append(current_record.strip())
    return data


import csv

# Use the custom parser to read the CSV file
csv_file_path = 'L&S.csv'
parsed_data = parse_custom_csv(csv_file_path)

# Convert the parsed data to CSV and save it
csv_file_path_new = 'L&S_new.csv'
with open(csv_file_path_new, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for record in parsed_data:
        # Assuming each record is a single column value. If not, you might need to split the record into fields
        writer.writerow([record])

print(f'CSV file saved to {csv_file_path_new}')

'''
# Use the custom parser to read the CSV file
csv_file_path = 'L&S.csv'
parsed_data = parse_custom_csv(csv_file_path)

# Convert the parsed data to JSON
json_data = json.dumps(parsed_data, indent=4)
json_file_path = 'L&S.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print(f'JSON file saved to {json_file_path}')
'''
