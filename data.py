# -*- coding:UTF-8 -*-
import re
import codecs
name = input()
f = codecs.open("/Users/zhang/PycharmProjects/noval spider/" + name + "_处理1.txt", "r", "utf-8")
fh = codecs.open("/Users/zhang/PycharmProjects/noval spider/" + name + "_处理2.txt", "w", "utf-8")
count = 0
alpha = re.compile(r'[a-zA-z0-9]')
for line in f.readlines():
    count += 1

    line = line.encode('utf-8').replace('！', '')
    line = line.replace('？', ' ')
    line = line.replace('?', ' ')
    line = line.replace(':', ' ')
    line = line.replace('!', ' ')
    line = line.replace('…', ' ')
    line = line.replace('。', ' ')
    line = line.replace('|', ' ')
    line = line.replace('-', '')
    line = line.replace('—', '')
    line = line.replace(',', ' ')
    line = line.replace('‘', '')
    line = line.replace('’', '')
    line = line.replace('.', ' ')
    line = line.replace('，', ' ')
    line = line.replace('：', ' ')
    line = line.replace('*', ' ')
    if alpha.findall(line):
        continue
    fh.write(line.decode('utf-8'))
print count