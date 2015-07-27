#coding:utf-8
import re
import string
import sys
import os
from datetime import *
#根据规则模板匹配微博

symbol = [" ", '"', "#", "＜", "＞", "“", "“", "≪", "" "≫", "「", "」", "《", "》", "【", "】", "（", "）", "<", ">", "[", "]"]
pos_p = []
neg_p = []
pos_full_name = []
neg_full_name = []
neg_verb_name1 = []
pos_verb_name1 = [] #type1: A.*B
pos_verb_name2 = [] #type2: AB
pos_verb_name3 = [] #type3: BA
neg_verb_name1.append("(看了|看过|看完)")

pos_verb_name1.append("(要|去|想|和|陪).{0,36}(看|睇)")
pos_verb_name1.append("(期待|坐等)")
pos_verb_name1.append("(出发|等看|看起|该看)")
pos_verb_name1.append("(一起看|组队看|求组|陪我看|陪看|陪同)")
pos_verb_name1.append("(来了|来啦|走起)")
pos_verb_name1.append("值得看")
pos_verb_name1.append("电影院")
pos_verb_name1.append("看定")
pos_verb_name1.append("(看起来|走起|得看|观影|奔向|首映|看电影)")
pos_verb_name2.append("(等待|等着看|等着)")
pos_verb_name1.append("我来")
pos_verb_name1.append("待观")
pos_verb_name2.append("好像.{0,36}看")
pos_verb_name2.append("希望.{0,36}看")
pos_verb_name2.append("来.{0,36}看")
#pos_verb_name2.append("看")
pos_verb_name2.append("(下午|今晚|明晚|明天|下周|过几天|过两天).{0,36}")
pos_verb_name2.append("(星期|礼拜)(一|二|三|四|五|六|日|天).{0,36}")
pos_verb_name2.append("(一|二|三|四|五|六|七|八|九|十|十一|十二)点.{0,36}")

pos_verb_name2.append("一起") #一起Movie_name，中间无间隔
pos_verb_name3.append("还是")

def match_for_movie(text,movie_name=""):
		for verb in neg_verb_name1:
				neg_full_name.append(verb + ".{0,36}" + movie_name)
				neg_full_name.append(movie_name + ".{0,36}" + verb)
		for verb in pos_verb_name1: #combination
				#if (pos_verb_name == "") #special
				pos_full_name.append(verb + ".{0,36}" + movie_name )
				pos_full_name.append(movie_name + ".{0,36}" + verb )
		for verb in pos_verb_name2:
				pos_full_name.append(verb + movie_name)
		for verb in pos_verb_name3:
				pos_full_name.append(movie_name + verb)
		pos_full_name.append("看" + movie_name + "去")
		for name in neg_full_name:
				neg_p.append(re.compile(name) )
		for name in pos_full_name:
				pos_p.append(re.compile(name) )

		is_match = judge(text)
		if (is_match == 1):
			return 1
		else:
			return 0
def judge(line):
		#预处理，去除《》【】（）<>()等等
		for s in symbol:
				line = line.replace(s, "")
		
		for pattern in neg_p:
				if (pattern.search(line) ):
						return 0
		for pattern in pos_p:
				if (pattern.search(line) ):
						return 1
		return 0
if (__name__ == '__main__'):
	new_movie = Movie(123,345,2012,9,26,'铜雀台')
	match_for_movie(new_movie)
