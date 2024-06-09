# To write a program that inserts commas after each letter and number in a file, you can follow these steps:

#  Read the content of the file.
# Process the content to insert commas.
# Write the modified content back to the file (or a new file).

def add_commas_to_file(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    
    # Insert commas after each letter and number
    modified_data = ",".join(list(data)) + ","
    
    with open(output_file, "w") as f:
        f.write(modified_data)

# Define the input and output file paths
input_file = "/home/dhiren/Documents/Codes/Python/MODULess/sample.txt"
output_file = "/home/dhiren/Documents/Codes/Python/MODULess/sample_with_commas.txt"

# Call the function to process the file
add_commas_to_file(input_file, output_file)
