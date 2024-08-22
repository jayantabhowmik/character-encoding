def find_non_latin1_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                line.encode('latin-1')
            except UnicodeEncodeError as e:
                print(f"Problematic character in line {line_number}: {e}")

file_path = 'path_to_your_log_file.log'
find_non_latin1_characters(file_path)
