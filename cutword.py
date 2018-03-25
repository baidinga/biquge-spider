# coding:utf-8
import jieba
import re
import codecs
name = input()
fread = codecs.open("/Users/zhang/PycharmProjects/noval spider/text/" + name + "_处理2.txt", "r", "utf-8")
fwrite = codecs.open("/Users/zhang/PycharmProjects/noval spider/style/" + name + "_风格.txt", "w", "utf-8")
count = 0
jieba.load_userdict("/Users/zhang/PycharmProjects/noval spider/name.txt")
name = []
ff = codecs.open("/Users/zhang/PycharmProjects/noval spider/name.txt", "r", "utf-8")


for line in fread.readlines():
    count += 1
    print count
    res_cut = jieba.cut(line, cut_all=False)
    fwrite.write(" ".join(res_cut))