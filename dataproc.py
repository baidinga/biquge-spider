# -*- coding:UTF-8 -*-
import re
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
alpha = re.compile(r'[a-zA-z0-9]')
name = input()
f = codecs.open('/Users/zhang/PycharmProjects/noval spider/' + name + '.txt', 'r', 'utf-8')
count = 0
fw = codecs.open('/Users/zhang/PycharmProjects/noval spider/' + name + '_.txt','w', "utf-8")

def delete_symbol(text):
    text = text.replace('！', '')
    text = text.replace('？', ' ')
    text = text.replace('?', ' ')
    text = text.replace(':', ' ')
    text = text.replace('!', ' ')
    text = text.replace('…', ' ')
    text = text.replace('。', ' ')
    text = text.replace('|', ' ')
    text = text.replace('-', '')
    text = text.replace('—', '')
    text = text.replace(',', ' ')
    text = text.replace('‘', '')
    text = text.replace('’', '')
    text = text.replace('.', ' ')
    text = text.replace('，', ' ')
    text = text.replace('：', ' ')
    text = text.replace('*', ' ')
    return text




for line in f.readlines():
    print line
    line = line.encode('utf-8').strip()
    count += 1
    if alpha.findall(line):
        continue
    if '“' in line or '”' in line or '手机访问' in line\
            or "推荐票" in line or "月票" in line or "一路看" in line or "[2]" in line or "VIP" in line or "笔下文学"\
            in line or "稍等片刻" in line or "笔趣" in line:
        continue
    str_divid = r'[。?!,]'
    divid = re.split(r"[。？！]", line)
    for text in divid:
        text = text.strip()
        text = delete_symbol(text)
        if len(text) < 150 and len(text) > 20:
            print text
            fw.write(text + '\n')

