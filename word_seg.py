# -*- coding: utf-8 -*-

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load("/Users/lzy/Code/ltp_model/cws.model")


def word_seg(line,label="0"):
	words = segmentor.segment(line)
	s=" ".join(words)
	return s