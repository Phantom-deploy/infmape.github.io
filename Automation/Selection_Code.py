def replace_placeholder(file_content, placeholder, replacement):
    return file_content.replace(placeholder, replacement)

def main():
    # Input file paths
    names_output_path = 'names_output.txt'
    pngoutput_path = 'pngoutput.txt'
    names_name_path = 'names_output.txt'

    # Output file path
    output_path = 'output.txt'

    # HTML template
    template_content = """
    <a href="Games/shadowgmes/[names_output.txt]/index.html" class="game-link container">
        <div class="game-tile">
            <img class="game-icon" src="Images/Shdowgmes/[pngoutput.txt]" alt="icon" loading="lazy" />
            <h1 class="game-title">[names_name.txt]</h1>
        </div>
    </a>
    """

    with open(names_output_path, 'r') as names_output_file, \
         open(pngoutput_path, 'r') as pngoutput_file, \
         open(names_name_path, 'r') as names_name_file:

        # Loop through the files line by line
        for names_output_line, pngoutput_line, names_name_line in zip(names_output_file, pngoutput_file, names_name_file):
            # Replace placeholders with actual lines
            replaced_content = replace_placeholder(template_content, '[names_output.txt]', names_output_line.strip())
            replaced_content = replace_placeholder(replaced_content, '[pngoutput.txt]', pngoutput_line.strip())
            replaced_content = replace_placeholder(replaced_content, '[names_name.txt]', names_name_line.strip())

            # Write the replaced content to the output file
            with open(output_path, 'a') as output_file:
                output_file.write(replaced_content + '\n')  # Add a new line after each iteration

if __name__ == "__main__":
    main()
