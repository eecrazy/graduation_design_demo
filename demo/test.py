#coding:utf8
from match import *
from word_seg import word_seg
from trim_stop_words import main
import os

def index(word):
	ret_data={}
	if not word:
		ret_data["result"]=None
	else:
		sig=match_for_movie(str(word))
		if sig==0:
			ret_data["str_result"]="该微博不含有消费意图!"
			ret_data["word"]=word
			return render_to_response("index.html",ret_data)
		ret="该微博含有对电影的消费意图\n\n"
		s=word_seg(str(word))
		#去除stopwords
		ss=main(s)
		#构建向量
		ret_data["str_result"]=ss
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
	return render_to_response("index.html",ret_data)

if __name__ == '__main__':
	index(word)