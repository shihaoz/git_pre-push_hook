import subprocess
import glob

# first compile the main program
cmd = ['g++', 'main.c', '-o', 'prog']
ret = subprocess.call(cmd)
if ret != 0:
	print 'failed compiling main.c, exiting'
	exit(1)
# remove the binary
subprocess.call(['rm', 'prog'])

blankline = '\n'
print 3 * blankline

# get all the files with test*.cpp
test_case = glob.glob('test*.cpp')
count_success = 0
count_failure = 0
for file_name in test_case:
	print 2*blankline
	cmd = ['g++', file_name, '-o', 'test']
	ret = subprocess.call(cmd)
	if ret != 0:
		print 'error compiling', file_name
		count_failure += 1
		continue

	ret = subprocess.call('./test')
	exec_name = file_name.split('.')[0]
	if ret != 0:
		print file_name, ' run failed!'
		count_failure += 1
		continue

	print 'test', exec_name, ' passed!'
	count_success += 1

print 3*blankline, 'feedback:'
print '   #sucess: ', count_success
print '   #failure: ', count_failure

if count_failure > 0:
	print 'Status: push failed'
	exit(1)

print 'Status: Compilation finished, ready to push'
# remove the binary
subprocess.call(['rm', 'test'])
