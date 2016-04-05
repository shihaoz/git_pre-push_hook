import glob
import Q2
searcher = Q2.Searcher()
for filename in searcher.search('algorithm', 2, glob.glob('*.txt')):
	print filename
