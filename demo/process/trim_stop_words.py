#coding:utf8

import sys
stop_hash={}

def main(line):
	for line in open("stop.words"):
		line=line.strip()
		# print line
		stop_hash[line]=1

	s=""
	line=line.strip().split()
	for word in line:
		if word in stop_hash:
			pass
		else:
			s+=word
			s+=" "
	# 		print word,
	# print ("")
	return s
