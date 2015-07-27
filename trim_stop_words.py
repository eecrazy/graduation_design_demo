#coding:utf8

import sys
import operator
stop_hash={}
ig1={}
ig2=[]
def main(line1,label):
	for line in open("stop.words"):
		line=line.strip()
		# print line
		stop_hash[line]=1

	s=[]
	line1=line1.strip().split()
	for word in line1:
		if word in stop_hash:
			pass
		else:
			s.append(word)
	# 		print word,
	# print ("")
	print label,
	print " ".join(s)
	for line in open("file_ig"):
		line=line.strip().split()
		ig1[line[0]]=int(line[1])
	sorted_word_hash = sorted(ig1.iteritems(), key=operator.itemgetter(1), reverse=False)

	# ss="1 "
	ss=str(label)
	ss+=" "
	for word in sorted_word_hash:
		ss+=str(word[1])
		ss+=":"
		if word[0] in s:
			ss+="1 "
		else:
			ss+="0 "
	p=open("test_file","a")
	p.write(ss)
	
	p.write("\n")
	# print ss
	return ss
