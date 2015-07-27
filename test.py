#coding:utf8
from match import *
from word_seg import word_seg
from trim_stop_words import main
import os

def index(word,label):
	ret_data={}
	if not word:
		return "hehe"
	else:
		sig=match_for_movie(str(word))
		if sig==0:
			return "该微博不含有消费意图!"
			ret_data["word"]=word
			# return render_to_response("index.html",ret_data)
		else:
			ret="该微博含有对电影的消费意图\n\n"
			s=word_seg(str(word))
			#去除stopwords
			ss=main(s,label)
			#构建向量
			# print ss
			#执行predict.sh进行预测
			os.system("sh predict.sh")
			for line in open("out"):
				line=line.strip().split()
				if line[0]=="labels":
					continue
				else:
					ret+="该消费意图转化为消费行为的概率为:"+line[1]+",不转化的概率为:"+line[2]
				break
			ret_data["str_result"]=ret
			ret_data["word"]=word
			# return render_to_response("index.html",ret_data)
			return ret

if __name__ == '__main__':
	for line in open("old_data"):
		line=line.strip().split()
		s=word_seg(str(line[3]),line[0])
		ss=main(s,line[0])
	os.system("sh predict.sh")
