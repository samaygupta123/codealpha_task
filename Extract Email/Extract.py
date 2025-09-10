import re
import os

INPUT_FILE = 'input/input.txt'
OUTPUT_FILE = 'output/emails.txt'

def extract_emails(input_path, output_path):
    if not os.path.exists('output'):
        os.makedirs('output')

    with open(input_path, 'r') as file:
        content = file.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    with open(output_path, 'w') as file:
        for email in sorted(set(emails)):
            file.write(email + '\n')

    print(f"✅ {len(emails)} email(s) extracted and saved to '{output_path}'.")

if __name__ == '__main__':
    extract_emails(INPUT_FILE, OUTPUT_FILE)
