import re
import os
import sys

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

arr = os.listdir(input_path)

for filename in arr:
	if filename[-4:] != '.svg':
		continue

	filepath = os.path.join(input_path,filename)

	with open(filepath, "r") as f:
		content = f.read()

	string = '<text fill="#eeeeee" stroke="none" font-family="Arial" font-size="24px" font-style="normal" font-weight="normal" text-decoration="none".*>UNREGISTERED</text>'
	x = re.search(string, content)

	new = content[:x.span()[0]] + content[x.span()[1]:]

	with open(filepath, "w") as f:
		f.write(new)
	print(filename + ': Watermark Removed')

sys.exit()