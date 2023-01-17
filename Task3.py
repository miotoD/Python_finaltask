import sys
import re
import random

def generate_email(student_id, name):
    surname,firstname = re.split(r'\s*,\s*', name)
    initials = '.'.join([x[0] for x in firstname.split()])
    surname = re.sub(r'[^a-zA-Z]+', '', surname)
    email = f'{initials}.{surname}{random.randint(1000, 9999)}@poppleton.ac.uk'
    return email.lower()

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    input_file = "student.txt"
    output_file = "emails.txt"
try:
    with open(input_file, "r") as f:
        lines = f.readlines()
    with open(output_file, "w") as f:
        for line in lines:
            student_id, name = line.split()[0], line.split()[1:]
            f.write(f'{student_id} {generate_email(student_id, " ".join(name))}\n')
except FileNotFoundError:
    print(f'Error: Cannot open {input_file} file. Sorry about that.')