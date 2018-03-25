# coding:utf-8
import codecs
name = input()
f = codecs.open("/Users/zhang/Desktop/ProjectCodes/data/" + name + "_风格的副本.txt", "r", "utf-8")
fh = codecs.open("/Users/zhang/Desktop/ProjectCodes/data/" + name + "_风格.txt", "w", "utf-8")
for line in f.readlines():
    if u"笔趣" in line:
        continue
    fh.write(line.strip() + '\n')