import urllib
import sys

test_cases_input = []
test_cases_output = []

def open_page(contestID, problemID):
	print "Trying to connect to the server..."
	pageURL = "http://www.codeforces.com/contest/" + contestID + "/problem/" + problemID
	print pageURL
	page = urllib.urlopen(pageURL)
	print "Connected to the server."
	print "Fetching Problem page..."
	source = page.read()

	return source

def generator(contestID, problemID):
	
	# with open('testpage.html', 'rt') as f:
	# 	source = f.read()

	source = open_page(contestID, problemID)

	print "Parsing problem page..."
	input_index = 0;
	output_index = 0;
	#input_index = source.find('''<span class="html-attribute-value">input</span>"&gt;''', input_index)
	input_index = source.find('''<div class="title">Input</div>''', input_index)
	if(input_index < 0):
		print "Error Parsing: No test cases found!"
	else:
		while(input_index > 0):
			
			input_index = source.find("<pre>", input_index)
			start_index = input_index + 5
			end_index = source.find('''</pre>''', start_index)
			input_string = source[start_index:end_index]
			input_string = input_string.replace('<br />', '\n')
			test_cases_input.append(input_string)
			input_index = end_index
			
			output_index = input_index
			#output_index = source.find('''<span class="html-attribute-value">output</span>"&gt;''', output_index)
			output_index = source.find('''<div class="title">Output</div>''', output_index)
			output_index = source.find('''<pre>''', output_index)
			start_index = output_index + 5
			end_index = source.find('''</pre>''', start_index)
			output_string = source[start_index:end_index]
			output_string = output_string.replace('<br />', '\n')
			test_cases_output.append(output_string)
			output_index = end_index

			input_index = source.find('''<div class="title">Input</div>''', input_index)

		with open('input.txt', 'wt') as inp:
			for i in test_cases_input:
				inp.write(i)

		with open('output.txt', 'wt') as out:
			for i in test_cases_output:
				out.write(i)


		print "Test cases parsed."
	
	return 0