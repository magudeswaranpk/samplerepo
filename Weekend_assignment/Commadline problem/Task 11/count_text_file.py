''' 11. Create a Python script that accepts a text file as a command-line argument
 and counts the number of words, lines, and characters in the file. '''


import sys

def count_words_lines_characters(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            line_count = text.count('\n') + 1  # Adding 1 to count the last line if it doesn't end with '\n'
            char_count = len(text)

            print(f"Word count: {word_count}")
            print(f"Line count: {line_count}")
            print(f"Character count: {char_count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_text_file.py <filename>")
    else:
        filename = sys.argv[1]
        count_words_lines_characters(filename)
