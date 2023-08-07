import json

# Read JSON data from input file
with open('input.json', 'r') as json_file:
    data = json.load(json_file)

# Read the text template
with open('template.txt', 'r') as template_file:
    template = template_file.read()

# Insert values into the template using string formatting
formatted_text = template.format(**data)

# Write the formatted text to the output file
with open('output.txt', 'w') as text_file:
    text_file.write(formatted_text)

print("Values from JSON have been inserted into the template and saved in output.txt")
