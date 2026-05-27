import json
file_content = ""
data = []
try:
    with open('../00_Beispieldateien/extracted.txt', 'r') as file:
        file_content = file.read()


except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")

# Simulated content of the file
if file_content:
# Process the content into a JSON format
    sections = file_content.strip().split('--------------------------------------------------------------------------------')


    for section in sections:
        if section.strip():
        # Split the section into title line and the message content
            lines = section.strip().split('\n', 1)
            name_line = lines[0].strip()
            message = lines[1].strip() if len(lines) > 1 else ""

        # Extract the name from the title line
            name = name_line.split(' (')[0].strip()
        
        # Append the dictionary to the data list
            data.append({"name": name, "message": message})

# Create the JSON structure
json_data = json.dumps(data, indent=2)

# Outputting the json to a file named output.json
output_file_path = "talk.json"
with open(output_file_path, "w") as file:
    file.write(json_data)

output_file_path
