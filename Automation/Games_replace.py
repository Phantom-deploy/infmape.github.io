import os

def process_html_files(file_path, output_file_path):
    # Read the input file
    with open(file_path, 'r') as input_file:
        # Filter lines with ".html" in them
        html_lines = [line.strip() for line in input_file if ".html" in line]

    # Create a string to store all the HTML code
    all_html_code = ""

    # Loop through each HTML file name
    for html_file_name in html_lines:
        # Generate the HTML content
        html_content = f'''<a href="Games/{html_file_name}" class="game-link container">
      <div class="game-tile">
        <img class="game-icon" src="images/Games/{html_file_name}" alt="icon" loading="lazy" />
        <h1 class="game-title">{html_file_name.replace('.html', '').title()}</h1>
      </div>
    </a>'''

        # Append the HTML content to the string
        all_html_code += html_content + "\n"

    # Write all the HTML code to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(all_html_code)

    print(f"File '{output_file_path}' created successfully!")

if __name__ == "__main__":
    # Specify the path to the input file
    input_file_path = "input_file.txt"  # Change this to your actual file path

    # Specify the path to the output file
    output_file_path = "output_file.html"  # Change this to your desired output file path

    # Check if the input file exists
    if os.path.exists(input_file_path):
        # Process the HTML files and write to the output file
        process_html_files(input_file_path, output_file_path)
    else:
        print(f"Error: File '{input_file_path}' not found.")
