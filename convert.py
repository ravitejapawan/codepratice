import os

def convert_txt_to_bash(input_file, output_file):
    # Read the contents of the input .txt file
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        content = infile.read()

    # Convert Windows line endings (\r\n) to Unix line endings (\n)
    content = content.replace('\r\n', '\n')

    # Write the content to the output .sh (bash) file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        outfile.write(content)

    # Make the .sh file executable (Linux/macOS)
    os.chmod(output_file, 0o755)

    print(f"Converted {input_file} to {output_file} with Unix-style line endings.")

# Usage
input_file = 'data.txt'  # Replace with your .txt file path
output_file = 'build_files.sh'  # The desired output .sh (bash script) file

convert_txt_to_bash(input_file, output_file)
