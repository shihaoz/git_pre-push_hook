import sys
# regular expression
import re

if len(sys.argv) < 4:
  print 'usage: <search word> <minimum appearance> <file_name1> ..'
  exit(1)

# get word and min appear
word = sys.argv[1]
min_count = int(sys.argv[2])

print 'args:', word, min_count

for idx in xrange(3, len(sys.argv)):
  file_name = sys.argv[idx]
  ifstream = open(file_name, 'rU')
  """
  USE regular expression to examine the file
  """
  pattern = r"{0}".format(word)	# interpret as raw string
  matches = re.findall(pattern, ifstream.read())

  if len(matches) >= min_count:
    print file_name
  ifstream.close()
