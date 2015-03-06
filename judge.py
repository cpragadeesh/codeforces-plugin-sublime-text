import subprocess
import os
import sys
import inputGen

def build():
	file_path = sys.argv[1]
	file_output_name = sys.argv[2]
	print 'Compiling...'
	compile_result = subprocess.call(['g++', file_path, '-o', file_path[:-4]])
	return compile_result

def verdict():
	contestID = sys.argv[2][:-1]
	problemID = sys.argv[2][-1]
	inputGen.generator(contestID, problemID)
	print 'Running test cases...\n'
	with open('input.txt', 'rt') as fin, open('output.txt') as fout:
		for linein, lineout in zip(fin, fout):
			with open('single_test_case.txt', 'wt') as f:
				f.write(linein)

			os.system('./' + contestID + problemID + ' < single_test_case.txt > single_out.txt')
			with open('single_out.txt', 'rt') as f:
				output = f.read()
				print 'Input:'
				linein = linein[:-1]
				print linein
				print 'Expected Output: '
				lineout = lineout[:-1]
				print lineout
				print 'Your Output:'
				print output
				print 'Verdict:',
				if(lineout == output):
					print 'CORRECT\n'
				else:
					print 'WRONG\n'
					print 'Incorrect Solution'
					return 0
		print "Correct Solution!"

def cleanup():
	os.system('rm Input.txt')
	os.system('rm output.txt')
	os.system('rm single_out.txt')
	os.system('rm single_test_case.txt')

result = build()
if result == 0:
	verdict()
	cleanup()
else:
	print 'Compilation Error.'