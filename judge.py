import subprocess
import os
from pageParser import *

def parse_page(contestID, problemID):
	parser = problemPageParser()
	source = open_page(contestID, problemID)
	parser.feed(source)
	test_cases = parser.return_data()
	return test_cases

def get_next_test_case(test_cases):
	test_cases = test_cases[1:]
	end = -1
	for i in test_cases:
		if i == 'Input':
			end = test_cases.index('Input')

	if end == -1:
		return test_cases, []
	else:
		end = test_cases.index('Input', 1)
		case = test_cases[:end]
		test_cases = test_cases[end:]
		return case, test_cases

def create_input_file(case):
	with open('input.txt', 'wt') as f:
		for i in case:
			if(i == 'Output'):
				break
			f.write(i + '\n')
	return case[:case.index('Output')]

def get_next_output(case):
	return case[case.index('Output') + 1:]

def build():

	file_output_name = sys.argv[1]
	file_path = sys.argv[2]
	file_out = file_path[:-4]
	print 'file_path: ', file_path
	print 'file_output_name: ', file_output_name
	print 'Compiling...'
	compile_result = subprocess.call(['g++', file_path, '-o', file_out])
	return compile_result

def verify(test_cases):
	case, test_cases = get_next_test_case(test_cases)
	input_case = create_input_file(case)
	expected_output = get_next_output(case)
	output = subprocess.check_output('./' + contestID + problemID + ' < input.txt', shell = True)
	print 'Output: ', output
	output_list = output.split('\n')
	if output_list[-1] == '':
		output_list = output_list[:-1]

	print ''
	print 'Input: '
	for inp in input_case:
		print inp
	print 'Your Output: '
	for out in output_list:
		print out
	print 'Expected output: '
	for op in expected_output:
		print op
	if output_list == expected_output:
		print 'Test case Passed!'
		return 0, test_cases, contestID, problemID
	else:
		print 'Wrong Answer!'
		return 1, test_cases, contestID, problemID

def run(test_cases, contestID, problemID):

	if len(test_cases) == 0:
		print ''
		print 'All test cases passed successfully!'
		return 0

	val, test_cases, problemID, contestID = verify(test_cases)

	if val == 0:
		run(test_cases, contestID, problemID)
	else:
		return 1

def cleanup():
	os.system('rm input.txt')

contestID = sys.argv[1][:-1]
problemID = sys.argv[1][-1]
build()
test_cases = parse_page(contestID, problemID)
run(test_cases, contestID, problemID)
cleanup()