import re
import os
import sys
import argparse


my_parser = argparse.ArgumentParser(
	usage = '%(prog)s  path [options]',
	description='Remove the starUML UNREGISTERED watermark from svg files in a folder')

my_parser.add_argument('path',
                       metavar='path',
                       type=str,
                       help='path to folder where svg files are stored')

my_parser.add_argument('--pdf',
                       action='store_true',
                       help='if specified produce a pdf version (default: only svg file)',
                       required=False)

args = my_parser.parse_args()

# check if path given exists
if not os.path.isdir(args.path):
    print('The path specified does not exist')
    sys.exit()

arr = os.listdir(args.path)

for filename in arr:
	if filename[-4:] != '.svg':
		continue

	filepath = os.path.join(args.path,filename)

	with open(filepath, "r") as f:
		content = f.read()

	string = '<text fill="#eeeeee" stroke="none" font-family="Arial" font-size="24px" font-style="normal" font-weight="normal" text-decoration="none".*>UNREGISTERED</text>'
	x = re.search(string, content)

	try:
		new = content[:x.span()[0]] + content[x.span()[1]:]
	except:
		continue


	with open(filepath, "w") as f:
		f.write(new)

	if args.pdf:
		try:
			from svglib.svglib import svg2rlg
			from reportlab.graphics import renderPDF
			drawing = svg2rlg(filepath)
			renderPDF.drawToFile(drawing, filepath[:-3]+"pdf" )
		except ImportError:
			print("Missing package: impossible to render pdf file")
		
		
	print(filename + ': Watermark Removed')

sys.exit()
