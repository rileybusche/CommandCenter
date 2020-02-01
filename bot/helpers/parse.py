# Parses stored linux command outputs
import subprocess

# def parse_for_output(text):
#     output = ''
#     for char in text:
#         output += char
#     return output    


metrics = subprocess.check_output('iostat', shell=True).decode('utf-8')

# output = parse_for_output(metrics)

print(metrics)
